# EVE Corp Navigator Bot v1.0.0

🚀 **Production-Ready Discord Bot for EVE Echoes Corporation Management**

## Features

✅ **Fixed CSV Exports** - One row per skill/ship with proper columns
✅ **Clone Selection UI** - Interactive dropdown for multi-clone users  
✅ **Stripe Payments** - Full payment processing with webhooks
✅ **Whitelist System** - Free premium for up to 5 guilds
✅ **Scalable Architecture** - Handles 2000 servers, 25K clones
✅ **Complete Data Management** - Skills, ships, events, members

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env with your tokens
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

## Environment Variables

Required:
- `DISCORD_TOKEN` - Your Discord bot token
- `MONGODB_URI` - MongoDB connection string
- `STRIPE_SECRET_KEY` - Stripe API key
- `STRIPE_WEBHOOK_SECRET` - Stripe webhook secret
- `STRIPE_PRICE_ID_MONTHLY` - Monthly subscription price ID
- `STRIPE_PRICE_ID_WEEKLY` - Weekly subscription price ID

Optional:
- `WHITELIST_GUILDS` - Comma-separated guild IDs (max 5)
- `PORT` - Web server port (default: 8000)
- `HOST` - Web server host (default: 0.0.0.0)

## Commands

### Admin
- `/setup` - Setup corporation
- `/stats` - View statistics  
- `/export_data` - Export data (CSV/JSON)
- `/members` - List members

### Members
- `/register` - Join/add clone
- `/profile` - View profile
- `/skills` - Manage skills
- `/ships` - Manage ships

### Premium
- `/upgrade` - Purchase premium

## Deployment

### Railway (Recommended)
```bash
railway login
railway init
railway up
```

### Heroku
```bash
heroku create
git push heroku main
```

### Docker
```bash
docker build -t eve-bot .
docker run -d --env-file .env eve-bot
```

## Support

Version: 1.0.0
Python: 3.10+
Discord.py: 2.3.2+

---
AGTD Official - All Rights Reserved
