"""
EVE Corp Navigator Bot v1.0.0 - Configuration
Central configuration with Stripe integration and whitelist support
"""

import os
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class Config:
    """Configuration manager for EVE Corp Navigator Bot"""

    # Bot Info
    BOT_VERSION = "1.0.0"
    BOT_PREFIX = os.getenv('BOT_PREFIX', '!')
    BOT_DESCRIPTION = "🚀 EVE Corp Navigator Bot v1.0.0 - Production Ready"

    # Discord
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    if not DISCORD_TOKEN:
        logger.warning("⚠️ DISCORD_TOKEN not set")

    # MongoDB
    MONGODB_URI = os.getenv('MONGODB_URI')
    if not MONGODB_URI:
        logger.warning("⚠️ MONGODB_URI not set")

    # Stripe Payment
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
    STRIPE_PRICE_ID_MONTHLY = os.getenv('STRIPE_PRICE_ID_MONTHLY')
    STRIPE_PRICE_ID_WEEKLY = os.getenv('STRIPE_PRICE_ID_WEEKLY')

    # Whitelist (Up to 5 guilds for free premium)
    WHITELIST_GUILDS_RAW = os.getenv('WHITELIST_GUILDS', '')
    WHITELIST_GUILDS: List[str] = [
        g.strip() for g in WHITELIST_GUILDS_RAW.split(',') if g.strip()
    ][:5]

    # Web Server
    WEB_PORT = int(os.getenv('PORT', 8000))
    WEB_HOST = os.getenv('HOST', '0.0.0.0')

    # Subscription Tiers
    SUBSCRIPTION_TIERS = {
        'free': {
            'max_corps': 1,
            'max_members_per_corp': 6,
            'max_clones_per_corp': 10,
            'advanced_analytics': False,
            'priority_support': False,
            'price': 0.00
        },
        'premium': {
            'max_corps': 999,
            'max_members_per_corp': 10000,
            'max_clones_per_corp': 25000,
            'advanced_analytics': True,
            'priority_support': True,
            'weekly_price': 2.00,
            'monthly_price': 6.00
        }
    }

    # Scalability Settings
    MONGODB_MAX_POOL_SIZE = 100
    MONGODB_MIN_POOL_SIZE = 10
    CACHE_TTL_SECONDS = 300
    RATE_LIMIT_PER_USER = 20

    @classmethod
    def is_whitelisted_guild(cls, guild_id: str) -> bool:
        """Check if guild is whitelisted"""
        return guild_id in cls.WHITELIST_GUILDS

    @classmethod
    def validate_stripe_config(cls) -> Dict[str, Any]:
        """Validate Stripe configuration"""
        validation = {'configured': True, 'missing': []}

        required = [
            ('STRIPE_SECRET_KEY', cls.STRIPE_SECRET_KEY),
            ('STRIPE_WEBHOOK_SECRET', cls.STRIPE_WEBHOOK_SECRET),
            ('STRIPE_PRICE_ID_MONTHLY', cls.STRIPE_PRICE_ID_MONTHLY),
            ('STRIPE_PRICE_ID_WEEKLY', cls.STRIPE_PRICE_ID_WEEKLY)
        ]

        for key_name, key_value in required:
            if not key_value:
                validation['configured'] = False
                validation['missing'].append(key_name)

        return validation

# Log configuration
if Config.WHITELIST_GUILDS:
    logger.info(f"✅ {len(Config.WHITELIST_GUILDS)} whitelisted guild(s)")

stripe_validation = Config.validate_stripe_config()
if not stripe_validation['configured']:
    logger.warning(f"⚠️ Stripe not configured: {stripe_validation['missing']}")
