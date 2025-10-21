"""
Subscription Manager for EVE Corp Navigator Bot v1.0.0
Handles premium subscriptions with Stripe integration
"""

import asyncio
from datetime import datetime, timezone, timedelta
from typing import Dict, Optional, Any
import logging
import stripe
from config import Config

logger = logging.getLogger(__name__)

class SubscriptionManager:
    """Manages premium subscriptions and payments"""

    def __init__(self, db_manager):
        self.db = db_manager

        # Initialize Stripe
        if Config.STRIPE_SECRET_KEY:
            stripe.api_key = Config.STRIPE_SECRET_KEY

    async def check_limits(self, user_id: str, guild_id: str, 
                          action: str, **kwargs) -> Dict[str, Any]:
        """Check if action is within subscription limits"""
        subscription = await self.db.get_user_subscription(user_id, guild_id)
        features = subscription.get('features', {})

        if action == 'add_member':
            max_members = features.get('max_members_per_corp', 6)
            current = kwargs.get('current_members', 0)
            allowed = current < max_members

        elif action == 'add_clone':
            max_clones = features.get('max_clones_per_corp', 10)
            current = kwargs.get('current_clones', 0)
            allowed = current < max_clones

        else:
            allowed = True

        return {
            'allowed': allowed,
            'tier': subscription.get('tier', 'free'),
            'features': features
        }

    async def create_checkout_session(self, user_id: str, guild_id: str,
                                     plan: str) -> Optional[str]:
        """Create Stripe Checkout session"""
        if not Config.STRIPE_SECRET_KEY:
            logger.error("Stripe not configured")
            return None

        try:
            price_id = (Config.STRIPE_PRICE_ID_MONTHLY if plan == 'monthly' 
                       else Config.STRIPE_PRICE_ID_WEEKLY)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='https://discord.com/channels/@me',
                cancel_url='https://discord.com/channels/@me',
                client_reference_id=user_id,
                metadata={
                    'discord_user_id': user_id,
                    'guild_id': guild_id,
                    'plan': plan
                }
            )

            return session.url

        except Exception as e:
            logger.error(f"Stripe checkout error: {e}")
            return None

    async def upgrade_user(self, user_id: str, plan: str, **kwargs) -> bool:
        """Upgrade user to premium"""
        try:
            result = await self.db.create_or_update_subscription(
                user_id=user_id,
                plan=plan,
                **kwargs
            )

            logger.info(f"✅ User {user_id} upgraded to {plan}")
            return result

        except Exception as e:
            logger.error(f"Upgrade error: {e}")
            return False

    async def cleanup_expired(self):
        """Clean up expired subscriptions"""
        try:
            # This would be implemented to batch update expired subscriptions
            logger.info("Running subscription cleanup...")
        except Exception as e:
            logger.error(f"Cleanup error: {e}")
