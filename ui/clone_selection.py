"""
Clone Selection UI for EVE Corp Navigator Bot v1.0.0
Interactive dropdown for selecting which clone to update
"""

import discord
from discord.ui import Select, View
from typing import Dict, List, Callable

class CloneSelectionView(View):
    """View with clone selection dropdown"""

    def __init__(self, member: Dict, callback_func: Callable, timeout: int = 300):
        super().__init__(timeout=timeout)
        self.member = member
        self.callback_func = callback_func
        self.selected_clone = None

        # Add dropdown
        self.add_item(CloneSelectDropdown(member, self.on_clone_selected))

    async def on_clone_selected(self, interaction: discord.Interaction, clone: Dict):
        """Callback when clone is selected"""
        self.selected_clone = clone
        await self.callback_func(interaction, clone)

class CloneSelectDropdown(Select):
    """Dropdown menu for clone selection"""

    def __init__(self, member: Dict, on_select: Callable):
        self.on_select_callback = on_select

        clones = member.get('clones', [])
        options = []

        for i, clone in enumerate(clones):
            # Primary clone gets crown emoji
            primary_badge = "👑 " if clone.get('is_primary', False) else ""

            options.append(discord.SelectOption(
                label=f"{primary_badge}{clone['name']}",
                description=f"{clone['empire']} | {clone['status']} | T{clone['tech_level']}",
                value=str(i),
                emoji="🧬"
            ))

        super().__init__(
            placeholder="Select which clone to update...",
            options=options,
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: discord.Interaction):
        """Handle dropdown selection"""
        selected_index = int(self.values[0])
        clone = self.view.member['clones'][selected_index]
        await self.on_select_callback(interaction, clone)
