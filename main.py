"""
EVE Corp Navigator Bot v1.0.0 - Main Entry Point
Production-ready Discord bot with all features
"""

import os
import logging
import asyncio
import threading
import discord
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
from datetime import datetime, timezone
import uvicorn
from contextlib import asynccontextmanager

# Load environment
load_dotenv()

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('bot.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

class EVECorpBot(commands.Bot):
    """Main bot class"""

    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            intents=intents,
            description="EVE Corp Navigator Bot v1.0.0"
        )
        self.db = None
        self.subscription_manager = None
        self.rate_limiter = None
        self.cache_manager = None

    async def setup_hook(self):
        """Initialize bot components"""
        logger.info("🔧 Initializing bot components...")

        # Initialize database
        from database.mongodb_manager import MongoDBManager
        self.db = MongoDBManager()
        await self.db.initialize()
        logger.info("✅ Database connected")

        # Initialize managers
        from utils.subscription_manager import SubscriptionManager
        from utils.rate_limiter import RateLimiter
        from utils.cache_manager import CacheManager

        self.subscription_manager = SubscriptionManager(self.db)
        self.rate_limiter = RateLimiter(max_per_minute=20)
        self.cache_manager = CacheManager(ttl_seconds=300)
        logger.info("✅ Managers initialized")

        # Load cogs
        await self.load_cogs()

        # Sync commands
        try:
            synced = await self.tree.sync()
            logger.info(f"✅ Synced {len(synced)} commands")
        except Exception as e:
            logger.error(f"❌ Failed to sync commands: {e}")

    async def load_cogs(self):
        """Load all command cogs"""
        cogs = [
            'commands.admin_commands',
            'commands.member_commands',
            'commands.skill_commands',
            'commands.ship_commands',
            'commands.event_commands',
            'commands.export_commands',
            'commands.payment_commands',
            'commands.timezone_commands',
            'commands.sync_commands'
        ]

        for cog in cogs:
            try:
                await self.load_extension(cog)
                logger.info(f"✅ Loaded {cog}")
            except Exception as e:
                logger.error(f"❌ Failed to load {cog}: {e}")

    async def on_ready(self):
        """Bot ready event"""
        logger.info("=" * 70)
        logger.info(f"🚀 EVE Corp Navigator Bot v1.0.0")
        logger.info(f"👤 Logged in as {self.user.name} ({self.user.id})")
        logger.info(f"🔗 Connected to {len(self.guilds)} guilds")
        logger.info("=" * 70)

        # Start background tasks
        self.cleanup_expired_subscriptions.start()
        self.update_bot_presence.start()

    @tasks.loop(hours=1)
    async def cleanup_expired_subscriptions(self):
        """Clean up expired subscriptions"""
        try:
            await self.subscription_manager.cleanup_expired()
        except Exception as e:
            logger.error(f"Subscription cleanup error: {e}")

    @tasks.loop(minutes=5)
    async def update_bot_presence(self):
        """Update bot presence"""
        try:
            guild_count = len(self.guilds)
            await self.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name=f"{guild_count} corporations | /help"
                )
            )
        except Exception as e:
            logger.error(f"Presence update error: {e}")

    async def on_guild_join(self, guild: discord.Guild):
        """Handle bot joining guild"""
        logger.info(f"✅ Joined guild: {guild.name} ({guild.id})")

        # Send welcome message
        try:
            channel = guild.system_channel or guild.text_channels[0]
            embed = discord.Embed(
                title="🚀 EVE Corp Navigator Bot",
                description=(
                    "Thanks for adding me!\n\n"
                    "**Get Started:**\n"
                    "1. Run `/setup` to create your corporation\n"
                    "2. Members can `/register` to join\n"
                    "3. Use `/help` for all commands\n\n"
                    "**Premium Features:**\n"
                    "Run `/upgrade` for unlimited members and clones!"
                ),
                color=0x00ff00
            )
            await channel.send(embed=embed)
        except:
            pass

    async def close(self):
        """Cleanup on shutdown"""
        logger.info("🛑 Shutting down...")
        if self.db:
            await self.db.close()
        await super().close()

# Initialize bot
bot = EVECorpBot()

# Web server for health checks and webhooks
@asynccontextmanager
async def lifespan(app):
    """FastAPI lifespan"""
    yield

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import stripe
from config import Config

# Initialize Stripe
if Config.STRIPE_SECRET_KEY:
    stripe.api_key = Config.STRIPE_SECRET_KEY

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "online",
        "version": "1.0.0",
        "guilds": len(bot.guilds) if bot.is_ready() else 0
    }

@app.post("/webhooks/stripe")
async def stripe_webhook(request: Request):
    """Handle Stripe webhooks"""
    if not Config.STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=500, detail="Webhook secret not configured")

    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, Config.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle events
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = session.get('metadata', {}).get('discord_user_id')
        plan = session.get('metadata', {}).get('plan')

        if user_id and plan:
            await bot.subscription_manager.upgrade_user(
                user_id=user_id,
                plan=plan,
                stripe_customer_id=session.get('customer'),
                stripe_subscription_id=session.get('subscription')
            )

            # Send confirmation DM
            try:
                user = await bot.fetch_user(int(user_id))
                await user.send(
                    f"✅ **Premium Activated!**\n\n"
                    f"Your {plan} subscription is now active.\n"
                    f"Enjoy unlimited features!"
                )
            except:
                pass

    return JSONResponse({"status": "success"})

def run_web_server():
    """Run FastAPI web server"""
    uvicorn.run(app, host=Config.WEB_HOST, port=Config.WEB_PORT)

def main():
    """Main entry point"""
    logger.info("🚀 Starting EVE Corp Navigator Bot v1.0.0...")

    # Start web server in background thread
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    logger.info(f"🌐 Web server started on {Config.WEB_HOST}:{Config.WEB_PORT}")

    # Run bot
    try:
        bot.run(Config.DISCORD_TOKEN)
    except KeyboardInterrupt:
        logger.info("🛑 Received shutdown signal")
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")

if __name__ == "__main__":
    main()
