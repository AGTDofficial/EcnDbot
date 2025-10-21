"""
Member Commands for EVE Corp Navigator Bot v1.0.0
Fixed profile display and clone management
"""

import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

class MemberCommands(commands.Cog):
    """Member management commands"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="register", description="🧬 Register or add clone")
    @app_commands.describe(
        clone_name="Your character name",
        empire="Caldari, Minmatar, Amarr, or Gallente",
        clone_status="Alpha or Omega",
        tech_level="Tech level 1-10"
    )
    async def register(
        self,
        interaction: discord.Interaction,
        clone_name: str,
        empire: str,
        clone_status: str,
        tech_level: int
    ):
        """Register member or add clone"""

        # Rate limit check
        if self.bot.rate_limiter.is_rate_limited(str(interaction.user.id)):
            await interaction.response.send_message(
                "⏰ Slow down! Try again in a moment.", 
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)
            user_id = str(interaction.user.id)

            # Check if corp exists
            corp = await self.bot.db.get_corporation_by_guild(guild_id)
            if not corp:
                await interaction.followup.send(
                    "❌ No corporation found! Admin must run `/setup` first.",
                    ephemeral=True
                )
                return

            # Check if member exists
            member = await self.bot.db.get_member(guild_id, user_id)

            # Prepare clone data
            clone_data = {
                'name': clone_name,
                'empire': empire,
                'status': clone_status,
                'tech_level': tech_level,
                'is_primary': member is None,  # First clone is primary
                'skills': {},
                'owned_ships': {},
                'created_at': datetime.now(timezone.utc),
                'updated_at': datetime.now(timezone.utc)
            }

            if member is None:
                # Create new member
                await self.bot.db.create_member(guild_id, user_id, clone_data)

                embed = discord.Embed(
                    title="✅ Registration Complete!",
                    description=f"Welcome to **{corp['name']}**, {interaction.user.mention}!",
                    color=0x00ff00
                )
                embed.add_field(name="Clone Name", value=clone_name)
                embed.add_field(name="Empire", value=empire)
                embed.add_field(name="Status", value=clone_status)
                embed.add_field(name="Tech Level", value=f"T{tech_level}")

            else:
                # Add additional clone
                success = await self.bot.db.add_clone_to_member(
                    guild_id, user_id, clone_data
                )

                if success:
                    embed = discord.Embed(
                        title="✅ Clone Added!",
                        description=f"New clone **{clone_name}** added to your account.",
                        color=0x00ff00
                    )
                    total_clones = len(member.get('clones', [])) + 1
                    embed.add_field(name="Total Clones", value=str(total_clones))
                else:
                    await interaction.followup.send(
                        "❌ Failed to add clone.", 
                        ephemeral=True
                    )
                    return

            await interaction.followup.send(embed=embed, ephemeral=True)

        except Exception as e:
            logger.error(f"Register error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}", 
                ephemeral=True
            )

    @app_commands.command(name="profile", description="👤 View your profile")
    async def profile(self, interaction: discord.Interaction):
        """View member profile - FIXED to show skills/ships correctly"""

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)
            user_id = str(interaction.user.id)

            member = await self.bot.db.get_member(guild_id, user_id)

            if not member:
                await interaction.followup.send(
                    "❌ You are not registered! Use `/register` first.",
                    ephemeral=True
                )
                return

            # Get clones
            clones = member.get('clones', [])

            # Find primary clone
            primary_clone = next(
                (c for c in clones if c.get('is_primary', False)),
                clones[0] if clones else {}
            )

            embed = discord.Embed(
                title=f"👤 {interaction.user.display_name}'s Profile",
                color=0x3498db
            )

            # Display primary clone info
            embed.add_field(
                name="Primary Clone",
                value=f"**{primary_clone.get('name', 'Unknown')}**\n"
                      f"{primary_clone.get('empire', 'Unknown')} | "
                      f"{primary_clone.get('status', 'Unknown')} | "
                      f"T{primary_clone.get('tech_level', 0)}",
                inline=False
            )

            # Count skills CORRECTLY (FIX)
            skill_count = 0
            skills_data = primary_clone.get('skills', {})
            for skill_type in skills_data.values():
                if isinstance(skill_type, dict):
                    for category in skill_type.values():
                        if isinstance(category, dict):
                            for subcategory in category.values():
                                if isinstance(subcategory, dict):
                                    skill_count += len(subcategory)

            # Count ships CORRECTLY (FIX)
            ship_count = 0
            ships_data = primary_clone.get('owned_ships', {})
            for ship_type in ships_data.values():
                if isinstance(ship_type, dict):
                    for subcategory in ship_type.values():
                        if isinstance(subcategory, list):
                            ship_count += len(subcategory)

            embed.add_field(name="Skills", value=str(skill_count), inline=True)
            embed.add_field(name="Ships", value=str(ship_count), inline=True)
            embed.add_field(name="Total Clones", value=str(len(clones)), inline=True)

            # List all clones
            if len(clones) > 1:
                clone_list = "\n".join([
                    f"{'👑 ' if c.get('is_primary') else ''}**{c['name']}** - {c['empire']}"
                    for c in clones
                ])
                embed.add_field(name="All Clones", value=clone_list, inline=False)

            await interaction.followup.send(embed=embed, ephemeral=True)

        except Exception as e:
            logger.error(f"Profile error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}", 
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(MemberCommands(bot))
