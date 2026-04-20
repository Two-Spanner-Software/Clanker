# pxsl :3
# dashcrikeydash

# i just want to say, we are sorry for writing some of the code in a terrible way.
# We are literally not cleaning ts up - pxsl

# anyway, now that the bot is open sourced, you can see how we are stealing all ur data and selling it to the highest bidder mwahahaha - pxsl

import discord
from discord.ext import commands, tasks
import asyncio
import os
import json
import time
import random

with open("data.json", "r") as f:
    data = json.load(f)

TOKEN = data.get("token")
if not TOKEN:
    raise ValueError("Token not found in data.json!")
    
TESTING = False
TEST_GUILD_ID = 1482405732329459754

cooldowns = {}

intents = discord.Intents.all()

class Clanker(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="lol this bot uses slash commands idot", # this literally does nothing im being serious lol - pxsl
            intents=intents
        )

    async def setup_hook(self):
        print("[BOOT] Loading cogs...")
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")
                print(f"[BOOT] Loaded cog: {file}")

        print("[BOOT] Syncing commands...")

        if TESTING:
            for i in range(5):
                print("[BOOT] Running in TESTING mode, syncing to TEST guild only.")

            guild = discord.Object(id=TEST_GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)

            print(f"[SYNC] Synced {len(synced)} commands to TEST guild")

            commands_data = []

            for cmd in self.tree.walk_commands():
                commands_data.append(cmd.to_dict(self.tree))

            with open("commands.json", "w") as f:
                json.dump(commands_data, f, indent=4)

            print(f"Exported {len(commands_data)} slash commands!")
        else:
            try:
                synced = await self.tree.sync()

                print("[SYNC] Cleared leftover commands from test guild")
            except Exception:
                pass

            synced = await self.tree.sync()
            print(f"[SYNC] Synced {len(synced)} global commands")
                        
            commands_data = []

            for cmd in self.tree.walk_commands():
                commands_data.append(cmd.to_dict(self.tree))

            with open("commands.json", "w") as f:
                json.dump(commands_data, f, indent=4)

            print(f"Exported {len(commands_data)} slash commands!")

        print("[BOOT] Status loop starting...")
        self.statusloop.start()

    @tasks.loop(minutes=5)
    async def statusloop(self):
        guild_count = len(self.guilds)
        await self.change_presence(
            activity=discord.CustomActivity(
                # HES CLANKING IT IN ME????? - dishcrackydosh (dw i like it)
                name=f"clanking in {guild_count} servers!"
            )
        )

    @statusloop.before_loop
    async def before_statusloop(self):
        await self.wait_until_ready()

bot = Clanker()
bot.data = data

@bot.event
async def on_ready():
    print(f"[READY] Logged in as {bot.user}")
    print("Clanker is alive 😎") # who the fuck put this stupid fucking shit ass fucking awful disgusting fucking shit emoji here

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.application_command:
        cmd = interaction.data.get("name")
        options = interaction.data.get("options", [])

        args = " ".join([opt["value"] for opt in options]) if options else ""

        print(f"[command log] @{interaction.user}: {cmd} {args}")

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())