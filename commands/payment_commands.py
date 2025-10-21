"""
Payment Commands for EVE Corp Navigator Bot v1.0.0
Stripe integration for premium subscriptions
"""

import discord
from discord.ext import commands
from discord import app_commands
import logging
from config import Config

logger = logging.getLogger(__name__)

class PaymentCommands(commands.Cog):
    """Premium subscription commands"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="upgrade", description="💎 Upgrade to Premium")
    @app_commands.describe(plan="Choose weekly or monthly plan")
    @app_commands.choices(plan=[
        app_commands.Choice(name="Weekly ($2.00/week)", value="weekly"),
        app_commands.Choice(name="Monthly ($6.00/month)", value="monthly")
    ])
    async def upgrade(self, interaction: discord.Interaction, plan: str):
        """Create Stripe checkout session for premium upgrade"""

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)
            user_id = str(interaction.user.id)

            # Check if already premium
            subscription = await self.bot.db.get_user_subscription(user_id, guild_id)

            if subscription.get('tier') == 'premium':
                if subscription.get('whitelisted'):
                    await interaction.followup.send(
                        "✨ You already have complimentary premium access!",
                        ephemeral=True
                    )
                else:
                    await interaction.followup.send(
                        f"✅ You already have premium (expires: {subscription.get('expires_at', 'Never')})",
                        ephemeral=True
                    )
                return

            # Create Stripe checkout session
            checkout_url = await self.bot.subscription_manager.create_checkout_session(
                user_id=user_id,
                guild_id=guild_id,
                plan=plan
            )

            if not checkout_url:
                await interaction.followup.send(
                    "❌ Payment system is not configured. Contact bot admin.",
                    ephemeral=True
                )
                return

            # Create embed with premium features
            price = "$2.00/week" if plan == "weekly" else "$6.00/month"

            embed = discord.Embed(
                title="💎 Upgrade to Premium",
                description=(
                    f"**{plan.capitalize()} Plan - {price}**\n\n"
                    "**Premium Features:**\n"
                    "✅ Unlimited corporations\n"
                    "✅ Up to 10,000 members\n"
                    "✅ Up to 25,000 clones\n"
                    "✅ Advanced analytics\n"
                    "✅ Priority support\n\n"
                    f"[**Click here to complete payment**]({checkout_url})"
                ),
                color=0xFFD700
            )

            embed.set_footer(text="Powered by Stripe • Secure Payment")

            await interaction.followup.send(embed=embed, ephemeral=True)

        except Exception as e:
            logger.error(f"Upgrade error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )

    @app_commands.command(name="subscription", description="📋 View your subscription")
    async def subscription(self, interaction: discord.Interaction):
        """View current subscription status"""

        await interaction.response.defer(ephemeral=True)

        try:
            guild_id = str(interaction.guild.id)
            user_id = str(interaction.user.id)

            subscription = await self.bot.db.get_user_subscription(user_id, guild_id)

            tier = subscription.get('tier', 'free')
            features = subscription.get('features', {})

            embed = discord.Embed(
                title="📋 Your Subscription",
                color=0xFFD700 if tier == 'premium' else 0x808080
            )

            if tier == 'premium':
                if subscription.get('whitelisted'):
                    embed.description = "✨ **Complimentary Premium Access**\nProvided by bot admin"
                else:
                    plan = subscription.get('plan', 'unknown')
                    expires = subscription.get('expires_at', 'Never')
                    embed.description = f"💎 **Premium {plan.capitalize()}**\nExpires: {expires}"
            else:
                embed.description = "🆓 **Free Tier**\nUpgrade to premium for more features!"

            embed.add_field(
                name="Max Members per Corp",
                value=str(features.get('max_members_per_corp', 6)),
                inline=True
            )
            embed.add_field(
                name="Max Clones per Corp",
                value=str(features.get('max_clones_per_corp', 10)),
                inline=True
            )
            embed.add_field(
                name="Advanced Analytics",
                value="✅" if features.get('advanced_analytics') else "❌",
                inline=True
            )

            if tier == 'free':
                embed.set_footer(text="Use /upgrade to get premium features!")

            await interaction.followup.send(embed=embed, ephemeral=True)

        except Exception as e:
            logger.error(f"Subscription view error: {e}")
            await interaction.followup.send(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(PaymentCommands(bot))
