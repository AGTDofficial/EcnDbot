# Changelog

## v1.0.0 (October 21, 2025)

### 🎉 Initial Release - Complete Rebuild

**Critical Fixes:**
- ✅ CSV export structure fixed - one row per skill/ship with separate columns
- ✅ Ship adding database updates fixed
- ✅ Profile display fixed to show skills and ships correctly
- ✅ Clone-specific data updates implemented

**New Features:**
- ✅ Clone selection UI for multi-clone users
- ✅ Stripe payment integration for premium subscriptions
- ✅ Whitelist system for up to 5 free premium guilds
- ✅ Rate limiting (20 commands/minute per user)
- ✅ Caching layer for performance
- ✅ Connection pooling for scalability

**Scalability:**
- ✅ MongoDB connection pooling (100 connections)
- ✅ Database indexing on all lookups
- ✅ Support for 2000 servers, 10K members, 25K clones
- ✅ Optimized for 300-500 concurrent users

**Architecture:**
- Discord.py 2.3.2+ with slash commands
- Motor async MongoDB driver
- FastAPI for webhooks and health checks
- Stripe API for payment processing

**Commands:**
- `/setup` - Create corporation (admin)
- `/register` - Join or add clone
- `/profile` - View profile with all clones
- `/skills` - Manage skills (with clone selection)
- `/ships` - Manage ships (with clone selection)
- `/export_data` - Export data (fixed CSV format)
- `/upgrade` - Purchase premium subscription
- `/subscription` - View subscription status
- `/stats` - Corporation statistics

**Environment Variables:**
- DISCORD_TOKEN - Required
- MONGODB_URI - Required
- STRIPE_SECRET_KEY - For payments
- STRIPE_WEBHOOK_SECRET - For payments
- STRIPE_PRICE_ID_MONTHLY - For payments
- STRIPE_PRICE_ID_WEEKLY - For payments
- WHITELIST_GUILDS - Up to 5 guild IDs (comma-separated)

**Deployment:**
- Compatible with Railway, Heroku, VPS
- Docker support included
- Render.yaml configuration included
