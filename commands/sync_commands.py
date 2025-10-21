"""
Sync Commands for EVE Corp Navigator Bot v1.0.0
"""

import discord
from discord.ext import commands
from discord import app_commands
import logging

logger = logging.getLogger(__name__)

class SyncCommands(commands.Cog):
    """Command syncing"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sync", description="🔄 Sync slash commands")
    async def sync(self, interaction: discord.Interaction):
        """Sync slash commands (owner only)"""

        if interaction.user.id != interaction.guild.owner_id:
            await interaction.response.send_message(
                "❌ Server owner only!",
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            synced = await self.bot.tree.sync()
            await interaction.followup.send(
                f"✅ Synced {len(synced)} commands!",
                ephemeral=True
            )
        except Exception as e:
            await interaction.followup.send(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(SyncCommands(bot))
