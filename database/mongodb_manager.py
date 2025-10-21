"""
MongoDB Manager for EVE Corp Navigator Bot v1.0.0
Complete async database operations with scalability optimizations
"""

import motor.motor_asyncio
from datetime import datetime, timezone, timedelta
import os
from typing import Dict, List, Optional, Any
import logging
from bson import ObjectId
from config import Config

logger = logging.getLogger(__name__)

class MongoDBManager:
    """MongoDB manager with connection pooling and indexing"""

    def __init__(self):
        self.client = None
        self.db = None
        self.corporations = None
        self.members = None
        self.events = None
        self.subscriptions = None

    async def initialize(self):
        """Initialize MongoDB with connection pooling"""
        try:
            mongodb_uri = Config.MONGODB_URI
            if not mongodb_uri:
                raise ValueError("MONGODB_URI required")

            # Connection with pooling for scalability
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                mongodb_uri,
                maxPoolSize=Config.MONGODB_MAX_POOL_SIZE,
                minPoolSize=Config.MONGODB_MIN_POOL_SIZE,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=10000
            )

            self.db = self.client.evecorp_navigator
            self.corporations = self.db.corporations
            self.members = self.db.members
            self.events = self.db.events
            self.subscriptions = self.db.subscriptions

            # Create indexes for performance
            await self._create_indexes()

            logger.info("✅ MongoDB initialized with connection pooling")

        except Exception as e:
            logger.error(f"❌ MongoDB initialization failed: {e}")
            raise

    async def _create_indexes(self):
        """Create database indexes for performance"""
        try:
            # Corporation indexes
            await self.corporations.create_index("guild_id", unique=True)

            # Member indexes (compound for guild+user lookups)
            await self.members.create_index(
                [("guild_id", 1), ("user_id", 1)], 
                unique=True
            )
            await self.members.create_index("guild_id")
            await self.members.create_index("user_id")

            # Event indexes
            await self.events.create_index([("guild_id", 1), ("event_time", 1)])
            await self.events.create_index("guild_id")

            # Subscription indexes
            await self.subscriptions.create_index("user_id", unique=True)
            await self.subscriptions.create_index("expires_at")

            logger.info("✅ Database indexes created")

        except Exception as e:
            logger.warning(f"⚠️ Index creation warning: {e}")

    # CORPORATION METHODS

    async def create_corporation(self, guild_id: str, name: str, 
                                created_by: str) -> Dict[str, Any]:
        """Create new corporation"""
        corp = {
            'guild_id': guild_id,
            'name': name,
            'created_by': created_by,
            'created_at': datetime.now(timezone.utc),
            'settings': {
                'max_members': 6,
                'max_clones': 10
            },
            'stats': {
                'total_members': 0,
                'total_clones': 0,
                'total_events': 0
            }
        }

        result = await self.corporations.insert_one(corp)
        corp['_id'] = result.inserted_id
        return corp

    async def get_corporation_by_guild(self, guild_id: str) -> Optional[Dict]:
        """Get corporation by guild ID"""
        return await self.corporations.find_one({'guild_id': guild_id})

    async def update_corporation_stats(self, guild_id: str, stats: Dict):
        """Update corporation statistics"""
        await self.corporations.update_one(
            {'guild_id': guild_id},
            {'$set': {'stats': stats}}
        )

    # MEMBER METHODS (FIXED)

    async def create_member(self, guild_id: str, user_id: str, 
                           clone_data: Dict) -> Dict[str, Any]:
        """Create new member with first clone"""
        member = {
            'guild_id': guild_id,
            'user_id': user_id,
            'clones': [clone_data],  # Array of clones
            'joined_at': datetime.now(timezone.utc),
            'role': 'member',
            'status': 'active',
            'metadata': {
                'last_active': datetime.now(timezone.utc)
            }
        }

        result = await self.members.insert_one(member)
        member['_id'] = result.inserted_id
        return member

    async def get_member(self, guild_id: str, user_id: str) -> Optional[Dict]:
        """Get member by guild and user ID"""
        return await self.members.find_one({
            'guild_id': guild_id,
            'user_id': user_id
        })

    async def add_clone_to_member(self, guild_id: str, user_id: str, 
                                  clone_data: Dict) -> bool:
        """Add additional clone to existing member (FIXED)"""
        result = await self.members.update_one(
            {'guild_id': guild_id, 'user_id': user_id},
            {
                '$push': {'clones': clone_data},
                '$set': {'metadata.last_active': datetime.now(timezone.utc)}
            }
        )
        return result.modified_count > 0

    async def get_all_members(self, guild_id: str) -> List[Dict]:
        """Get all members in corporation"""
        cursor = self.members.find({'guild_id': guild_id})
        return await cursor.to_list(length=None)

    # CLONE-SPECIFIC METHODS (NEW - FIX FOR PROFILE/EXPORT)

    async def update_clone_skills(self, guild_id: str, user_id: str,
                                  clone_name: str, skills: Dict) -> bool:
        """Update skills for specific clone (FIXED)"""
        result = await self.members.update_one(
            {
                'guild_id': guild_id,
                'user_id': user_id,
                'clones.name': clone_name
            },
            {
                '$set': {
                    'clones.$.skills': skills,
                    'clones.$.updated_at': datetime.now(timezone.utc)
                }
            }
        )
        return result.modified_count > 0

    async def update_clone_ships(self, guild_id: str, user_id: str,
                                clone_name: str, ships: Dict) -> bool:
        """Update ships for specific clone (FIXED)"""
        result = await self.members.update_one(
            {
                'guild_id': guild_id,
                'user_id': user_id,
                'clones.name': clone_name
            },
            {
                '$set': {
                    'clones.$.owned_ships': ships,
                    'clones.$.ships_updated_at': datetime.now(timezone.utc)
                }
            }
        )
        return result.modified_count > 0

    async def get_clone_by_name(self, guild_id: str, user_id: str,
                               clone_name: str) -> Optional[Dict]:
        """Get specific clone from member"""
        member = await self.get_member(guild_id, user_id)
        if member and 'clones' in member:
            for clone in member['clones']:
                if clone.get('name') == clone_name:
                    return clone
        return None

    # SUBSCRIPTION METHODS (WITH WHITELIST)

    async def get_user_subscription(self, user_id: str, 
                                   guild_id: str = None) -> Dict[str, Any]:
        """Get user subscription (checks whitelist first)"""
        # Check whitelist
        if guild_id and Config.is_whitelisted_guild(guild_id):
            return {
                'user_id': user_id,
                'tier': 'premium',
                'is_active': True,
                'whitelisted': True,
                'features': Config.SUBSCRIPTION_TIERS['premium'],
                'expires_at': None
            }

        # Check regular subscription
        sub = await self.subscriptions.find_one({'user_id': user_id})

        if not sub:
            # Free tier
            return {
                'user_id': user_id,
                'tier': 'free',
                'is_active': True,
                'features': Config.SUBSCRIPTION_TIERS['free'],
                'expires_at': None
            }

        # Check if expired
        if sub.get('expires_at'):
            if datetime.now(timezone.utc) > sub['expires_at']:
                sub['is_active'] = False
                sub['tier'] = 'free'
                sub['features'] = Config.SUBSCRIPTION_TIERS['free']

        return sub

    async def create_or_update_subscription(self, user_id: str, 
                                           plan: str, **kwargs) -> bool:
        """Create or update user subscription"""
        expires_at = None
        if plan == 'weekly':
            expires_at = datetime.now(timezone.utc) + timedelta(days=7)
        elif plan == 'monthly':
            expires_at = datetime.now(timezone.utc) + timedelta(days=30)

        subscription = {
            'user_id': user_id,
            'tier': 'premium',
            'plan': plan,
            'is_active': True,
            'features': Config.SUBSCRIPTION_TIERS['premium'],
            'expires_at': expires_at,
            'updated_at': datetime.now(timezone.utc),
            **kwargs
        }

        result = await self.subscriptions.update_one(
            {'user_id': user_id},
            {'$set': subscription},
            upsert=True
        )

        return result.modified_count > 0 or result.upserted_id is not None

    # EVENT METHODS

    async def create_event(self, guild_id: str, event_data: Dict) -> Dict:
        """Create new event"""
        event = {
            'guild_id': guild_id,
            'created_at': datetime.now(timezone.utc),
            **event_data
        }

        result = await self.events.insert_one(event)
        event['_id'] = result.inserted_id
        return event

    async def get_guild_events(self, guild_id: str) -> List[Dict]:
        """Get all events for guild"""
        cursor = self.events.find({'guild_id': guild_id}).sort('event_time', 1)
        return await cursor.to_list(length=None)

    async def close(self):
        """Close database connection"""
        if self.client:
            self.client.close()
            logger.info("✅ MongoDB connection closed")
