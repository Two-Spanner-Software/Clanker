from discord import app_commands, Interaction
from discord.ext import commands
import discord
import json

def owner_check():
    async def predicate(interaction: Interaction):
        return interaction.user.id in interaction.client.data.get("owners", [])
    return app_commands.check(predicate)

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def save_data(self):
        with open("data.json", "w") as f:
            json.dump(self.bot.data, f, indent=4)

    @app_commands.command(name="addadmin", description="(OWNER) give someone admin")
    @owner_check()
    async def addadmin(self, interaction: Interaction, user: discord.Member):

        if user.id in self.bot.data.get("admins", []):
            await interaction.response.send_message(
                "Already an admin.",
                ephemeral=True
            )
            return

        self.bot.data.setdefault("admins", []).append(user.id)
        self.save_data()

        await interaction.response.send_message(
            f"{user.mention} is now an admin.",
            ephemeral=True
        )

    @app_commands.command(name="removeadmin", description="(OWNER) remove admin")
    @owner_check()
    async def removeadmin(self, interaction: Interaction, user: discord.Member):

        if user.id not in self.bot.data.get("admins", []):
            await interaction.response.send_message(
                "Not an admin.",
                ephemeral=True
            )
            return

        self.bot.data["admins"].remove(user.id)
        self.save_data()

        await interaction.response.send_message(
            f"{user.mention} is no longer an admin.",
            ephemeral=True
        )

    @app_commands.command(name="listadmins", description="(OWNER) list admins")
    @owner_check()
    async def listadmins(self, interaction: Interaction):

        admins = self.bot.data.get("admins", [])

        if not admins:
            await interaction.response.send_message(
                "No admins set.",
                ephemeral=True
            )
            return

        mentions = [f"<@{uid}>" for uid in admins]

        embed = discord.Embed(
            title="Admins",
            description="\n".join(mentions),
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

    @addadmin.error
    @removeadmin.error
    @listadmins.error
    async def admin_error(self, interaction: Interaction, error):

        if isinstance(error, app_commands.errors.CheckFailure):
            await interaction.response.send_message(
                "You are not allowed to use this.",
                ephemeral=True
            )
        else:
            if not interaction.response.is_done():
                await interaction.response.send_message(
                    "Something went wrong.",
                    ephemeral=True
                )
            raise error
    
    @app_commands.command(name="license", description="(OWNER) send a license troll message to a channel")
    async def license(self, interaction: Interaction, channel: discord.TextChannel):

        if interaction.user.id not in self.bot.data.get("admins", []) and interaction.user.id not in self.bot.data.get("owners", []):
            await interaction.response.send_message("No permission.", ephemeral=True)
            return

        class RenewView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=60)

            @discord.ui.button(label="Renew License", style=discord.ButtonStyle.red)
            async def renew(self, interaction_btn: Interaction, button: discord.ui.Button):
                await interaction_btn.message.delete()
                await interaction_btn.response.send_message(
                    "haha lol trolled by the bot admins imagine",
                    ephemeral=True
                )
                self.stop()

        view = RenewView()

        embed = discord.Embed(
            title="⚠️ License Expired",
            description=(
                "Sorry! Your license is now outdated!\n\n"
                "Click the button below to renew it."
            ),
            color=discord.Color.red()
        )

        try:
            await channel.send(embed=embed, view=view)

            await interaction.response.send_message(
                f"📩 Sent license message to {channel.mention}",
                ephemeral=True
            )

        except discord.Forbidden:
            await interaction.response.send_message(
                "I can't send messages in that channel.",
                ephemeral=True
            )
    
    @app_commands.command(name="give", description="(OWNER) give someone money")
    @app_commands.describe(user="who to give money to", amount="amount to give")
    @owner_check()
    async def give(self, interaction: Interaction, user: discord.Member, amount: int):

        if amount <= 0:
            return await interaction.response.send_message("Amount must be > 0.", ephemeral=True)

        economy = self.bot.get_cog("Economy")
        if not economy:
            return await interaction.response.send_message("Economy cog not loaded.", ephemeral=True)

        row = economy.get_user(interaction.guild.id, user.id)
        target = economy.user_dict(row)

        target["balance"] += amount
        economy.update_user(target)

        embed = discord.Embed(
            title="💰 Money Given",
            description=f"Gave **{amount} coins** to {user.mention}",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="take", description="(OWNER) remove money from someone")
    @app_commands.describe(user="who to take money from", amount="amount to remove")
    @owner_check()
    async def take(self, interaction: Interaction, user: discord.Member, amount: int):

        if amount <= 0:
            return await interaction.response.send_message("Amount must be > 0.", ephemeral=True)

        economy = self.bot.get_cog("Economy")
        if not economy:
            return await interaction.response.send_message("Economy cog not loaded.", ephemeral=True)

        row = economy.get_user(interaction.guild.id, user.id)
        target = economy.user_dict(row)

        removed = min(amount, target["balance"])
        target["balance"] -= removed

        economy.update_user(target)

        embed = discord.Embed(
            title="💸 Money Removed",
            description=f"Removed **{removed} coins** from {user.mention}",
            color=discord.Color.red()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="dm", description="(OWNER) send a DM to a user")
    @app_commands.describe(
        user="user to DM",
        title="embed title",
        message="embed description"
    )
    @owner_check()
    async def dm(self, interaction: Interaction, user: discord.User, title: str, message: str):

        try:
            dm_channel = await user.create_dm()

            embed = discord.Embed(
                title=title,
                description=message,
                color=discord.Color.blurple()
            )

            await dm_channel.send(embed=embed)

            await interaction.response.send_message(
                f"📩 Sent DM to {user.mention}",
                ephemeral=True
            )

        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ I can't DM this user (DMs closed).",
                ephemeral=True
            )

    @app_commands.command(name="broadcast", description="(OWNER) send a message to all servers' mod logs channels")
    @app_commands.describe(title="embed title", message="embed message")
    @owner_check()
    async def broadcast(self, interaction: Interaction, title: str, message: str):

        sent = 0
        failed = 0

        embed = discord.Embed(
            title=title,
            description=message,
            color=discord.Color.blurple()
        )

        for guild in self.bot.guilds:

            channel = guild.system_channel

            if channel is None:
                channel = discord.utils.get(guild.text_channels, name="mod-logs") or \
                        discord.utils.get(guild.text_channels, name="modlogs") or \
                        discord.utils.get(guild.text_channels, name="mod-log")

            if channel is None:
                failed += 1
                continue

            try:
                await channel.send(embed=embed)
                sent += 1
            except discord.Forbidden:
                failed += 1

        await interaction.response.send_message(
            f"📡 Broadcast complete\n"
            f"✅ Sent: {sent}\n"
            f"❌ Failed: {failed}",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Admin(bot))
