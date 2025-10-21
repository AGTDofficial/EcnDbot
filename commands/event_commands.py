"""
Event Commands - Placeholder
"""
from discord.ext import commands

class EventCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(EventCommands(bot))
