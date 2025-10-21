"""
Admin Commands for EVE Corp Navigator Bot v1.0.0
Corporation setup and management
"""

import discord
from discord.ext import commands
from discord import app_commands
import logging

logger = logging.getLogger(__name__)

class AdminCommands(commands.Cog):
    """Administrator commands"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setup", description="⚙️ Setup corporation")
    @app_commands.describe(corp_name="Corporation name")
    async def setup(self, interaction: discord.Interaction, corp_name: str):
        """Setup corporation"""

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ Admin only!", 
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)

            # Check if already exists
            existing = await self.bot.db.get_corporation_by_guild(guild_id)
            if existing:
                await interaction.followup.send(
                    f"✅ Corporation **{existing['name']}** already exists!",
                    ephemeral=True
                )
                return

            # Create corporation
            corp = await self.bot.db.create_corporation(
                guild_id=guild_id,
                name=corp_name,
                created_by=str(interaction.user.id)
            )

            embed = discord.Embed(
                title="✅ Corporation Created!",
                description=f"**{corp_name}** is ready for members.",
                color=0x00ff00
            )
            embed.add_field(
                name="Next Steps",
                value=(
                    "1️⃣ Members use `/register` to join\n"
                    "2️⃣ Add skills with `/skills`\n"
                    "3️⃣ Add ships with `/ships`\n"
                    "4️⃣ View stats with `/stats`"
                ),
                inline=False
            )

            await interaction.followup.send(embed=embed, ephemeral=True)

        except Exception as e:
            logger.error(f"Setup error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )

    @app_commands.command(name="stats", description="📊 Corporation statistics")
    async def stats(self, interaction: discord.Interaction):
        """View corporation statistics"""

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)

            corp = await self.bot.db.get_corporation_by_guild(guild_id)
            if not corp:
                await interaction.followup.send(
                    "❌ No corporation found!",
                    ephemeral=True
                )
                return

            members = await self.bot.db.get_all_members(guild_id)

            total_clones = sum(len(m.get('clones', [])) for m in members)

            embed = discord.Embed(
                title=f"📊 {corp['name']} Statistics",
                color=0x3498db
            )
            embed.add_field(name="Total Members", value=str(len(members)), inline=True)
            embed.add_field(name="Total Clones", value=str(total_clones), inline=True)
            embed.add_field(name="Created", value=corp['created_at'].strftime('%Y-%m-%d'), inline=True)

            await interaction.followup.send(embed=embed, ephemeral=True)

        except Exception as e:
            logger.error(f"Stats error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
