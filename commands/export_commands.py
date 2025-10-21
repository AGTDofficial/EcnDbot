"""
Export Commands for EVE Corp Navigator Bot v1.0.0
CRITICAL FIX: Proper CSV structure with one row per skill/ship
"""

import discord
from discord.ext import commands
from discord import app_commands
import logging
import csv
import io
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

class ExportCommands(commands.Cog):
    """Data export commands with fixed CSV structure"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="export_data", description="📊 Export corporation data")
    async def export_data(self, interaction: discord.Interaction):
        """Export data with proper CSV format (FIXED)"""

        # Check admin
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ Admin only!", 
                ephemeral=True
            )
            return

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)
            members = await self.bot.db.get_all_members(guild_id)

            if not members:
                await interaction.followup.send(
                    "❌ No members found!", 
                    ephemeral=True
                )
                return

            # Generate CSV files
            skills_csv = await self._export_skills_csv(members)
            ships_csv = await self._export_ships_csv(members)
            detailed_csv = await self._export_detailed_csv(members)

            # Send files
            await interaction.followup.send(
                "📊 **Export Complete!**\n\n"
                "Attached files:\n"
                "• **skills.csv** - One row per skill\n"
                "• **ships.csv** - One row per ship\n"
                "• **detailed.csv** - Complete member data",
                files=[
                    discord.File(skills_csv, filename="skills_export.csv"),
                    discord.File(ships_csv, filename="ships_export.csv"),
                    discord.File(detailed_csv, filename="detailed_export.csv")
                ],
                ephemeral=True
            )

        except Exception as e:
            logger.error(f"Export error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}", 
                ephemeral=True
            )

    async def _export_skills_csv(self, members) -> io.BytesIO:
        """Export skills - ONE ROW PER SKILL (CRITICAL FIX)"""

        output = io.StringIO()
        writer = csv.writer(output)

        # Headers - SEPARATE COLUMNS FOR EACH LEVEL
        writer.writerow([
            'User ID', 'Discord Name', 'Clone Name', 'Empire', 'Tech Level',
            'Skill Type', 'Category', 'Subcategory', 'Skill Name',
            'Level 1', 'Level 2', 'Level 3', 'Updated At'
        ])

        # Write data - ONE ROW PER SKILL
        for member in members:
            user_id = member.get('user_id', '')

            for clone in member.get('clones', []):
                clone_name = clone.get('name', '')
                empire = clone.get('empire', '')
                tech_level = clone.get('tech_level', 0)

                skills = clone.get('skills', {})

                # Iterate through skill structure
                for skill_type, categories in skills.items():
                    if not isinstance(categories, dict):
                        continue

                    for category, subcategories in categories.items():
                        if not isinstance(subcategories, dict):
                            continue

                        for subcategory, skill_list in subcategories.items():
                            if not isinstance(skill_list, dict):
                                continue

                            # Each skill gets its own row
                            for skill_name, skill_data in skill_list.items():

                                # Parse level string "5/5/4" into separate columns
                                level_str = skill_data.get('level', '0/0/0')
                                level_parts = level_str.split('/')
                                level1 = level_parts[0] if len(level_parts) > 0 else '0'
                                level2 = level_parts[1] if len(level_parts) > 1 else '0'
                                level3 = level_parts[2] if len(level_parts) > 2 else '0'

                                updated = skill_data.get('updated_at', '')

                                writer.writerow([
                                    user_id,
                                    '',  # Discord name (filled by bot)
                                    clone_name,
                                    empire,
                                    tech_level,
                                    skill_type,
                                    category,
                                    subcategory,
                                    skill_name,
                                    level1,  # Separate column
                                    level2,  # Separate column
                                    level3,  # Separate column
                                    str(updated)
                                ])

        # Convert to bytes
        output.seek(0)
        return io.BytesIO(output.getvalue().encode('utf-8'))

    async def _export_ships_csv(self, members) -> io.BytesIO:
        """Export ships - ONE ROW PER SHIP (FIXED)"""

        output = io.StringIO()
        writer = csv.writer(output)

        # Headers
        writer.writerow([
            'User ID', 'Discord Name', 'Clone Name', 'Empire', 'Tech Level',
            'Ship Type', 'Subcategory', 'Ship Name', 'Updated At'
        ])

        # Write data - ONE ROW PER SHIP
        for member in members:
            user_id = member.get('user_id', '')

            for clone in member.get('clones', []):
                clone_name = clone.get('name', '')
                empire = clone.get('empire', '')
                tech_level = clone.get('tech_level', 0)

                ships = clone.get('owned_ships', {})

                # Iterate through ship structure
                for ship_type, subcategories in ships.items():
                    if not isinstance(subcategories, dict):
                        continue

                    for subcategory, ship_list in subcategories.items():
                        if not isinstance(ship_list, list):
                            continue

                        # Each ship gets its own row
                        for ship_name in ship_list:
                            writer.writerow([
                                user_id,
                                '',  # Discord name
                                clone_name,
                                empire,
                                tech_level,
                                ship_type,
                                subcategory,
                                ship_name,
                                str(clone.get('ships_updated_at', ''))
                            ])

        # Convert to bytes
        output.seek(0)
        return io.BytesIO(output.getvalue().encode('utf-8'))

    async def _export_detailed_csv(self, members) -> io.BytesIO:
        """Export detailed member data"""

        output = io.StringIO()
        writer = csv.writer(output)

        # Headers
        writer.writerow([
            'User ID', 'Clone Name', 'Empire', 'Status', 'Tech Level',
            'Total Skills', 'Total Ships', 'Joined At', 'Last Active'
        ])

        # Write data
        for member in members:
            user_id = member.get('user_id', '')
            joined = member.get('joined_at', '')
            last_active = member.get('metadata', {}).get('last_active', '')

            for clone in member.get('clones', []):
                # Count skills
                skill_count = 0
                skills = clone.get('skills', {})
                for skill_type in skills.values():
                    if isinstance(skill_type, dict):
                        for category in skill_type.values():
                            if isinstance(category, dict):
                                for subcategory in category.values():
                                    if isinstance(subcategory, dict):
                                        skill_count += len(subcategory)

                # Count ships
                ship_count = 0
                ships = clone.get('owned_ships', {})
                for ship_type in ships.values():
                    if isinstance(ship_type, dict):
                        for subcategory in ship_type.values():
                            if isinstance(subcategory, list):
                                ship_count += len(subcategory)

                writer.writerow([
                    user_id,
                    clone.get('name', ''),
                    clone.get('empire', ''),
                    clone.get('status', ''),
                    clone.get('tech_level', 0),
                    skill_count,
                    ship_count,
                    str(joined),
                    str(last_active)
                ])

        # Convert to bytes
        output.seek(0)
        return io.BytesIO(output.getvalue().encode('utf-8'))

async def setup(bot):
    await bot.add_cog(ExportCommands(bot))
