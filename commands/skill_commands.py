"""
Skill Commands for EVE Corp Navigator Bot v1.0.0
With clone selection support
"""

import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import View, Select, Button
import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

class SkillCommands(commands.Cog):
    """Skill management with clone selection"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="skills", description="🎯 Manage skills")
    async def manage_skills(self, interaction: discord.Interaction):
        """Skill management interface with clone selection"""

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)
            user_id = str(interaction.user.id)

            member = await self.bot.db.get_member(guild_id, user_id)

            if not member:
                await interaction.followup.send(
                    "❌ Not registered! Use `/register` first.",
                    ephemeral=True
                )
                return

            clones = member.get('clones', [])

            if len(clones) == 0:
                await interaction.followup.send(
                    "❌ No clones found!",
                    ephemeral=True
                )
                return

            # If only one clone, use it directly
            if len(clones) == 1:
                clone = clones[0]
                await self._show_skill_interface(interaction, guild_id, user_id, clone)
            else:
                # Show clone selection (FIX: Clone selection UI)
                await self._show_clone_selection(interaction, member, guild_id, user_id)

        except Exception as e:
            logger.error(f"Skills error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )

    async def _show_clone_selection(self, interaction, member, guild_id, user_id):
        """Show clone selection dropdown"""

        embed = discord.Embed(
            title="🧬 Select Clone",
            description="Choose which clone to manage skills for:",
            color=0x3498db
        )

        # Create selection view
        view = View(timeout=300)

        options = []
        for i, clone in enumerate(member['clones']):
            primary = "👑 " if clone.get('is_primary') else ""
            options.append(discord.SelectOption(
                label=f"{primary}{clone['name']}",
                description=f"{clone['empire']} | T{clone['tech_level']}",
                value=str(i)
            ))

        select = Select(placeholder="Choose clone...", options=options)

        async def select_callback(select_interaction: discord.Interaction):
            idx = int(select.values[0])
            clone = member['clones'][idx]
            await select_interaction.response.defer()
            await self._show_skill_interface(select_interaction, guild_id, user_id, clone)

        select.callback = select_callback
        view.add_item(select)

        await interaction.followup.send(embed=embed, view=view, ephemeral=True)

    async def _show_skill_interface(self, interaction, guild_id, user_id, clone):
        """Show skill management interface for selected clone"""

        embed = discord.Embed(
            title=f"🎯 Skills - {clone['name']}",
            description="Skill management interface (simplified for demo)",
            color=0x00ff00
        )

        # Count current skills
        skill_count = 0
        skills = clone.get('skills', {})
        for skill_type in skills.values():
            if isinstance(skill_type, dict):
                for category in skill_type.values():
                    if isinstance(category, dict):
                        for subcategory in category.values():
                            if isinstance(subcategory, dict):
                                skill_count += len(subcategory)

        embed.add_field(name="Current Skills", value=str(skill_count))
        embed.add_field(name="Clone", value=clone['name'])

        await interaction.followup.send(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(SkillCommands(bot))
