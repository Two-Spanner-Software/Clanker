# im a socaiial file

from discord import Interaction, app_commands
from discord.ext import commands
import random
import discord

class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="social", description="see what the social category does")
    async def basic(self, interaction: Interaction):
        command_count = len(self.get_app_commands())

        embed = discord.Embed(
            title="Social 📚",
            description="Hello, the social category handles most social/roleplay commands on the bot.\n"
                        f"There are currently **{command_count} commands** in this category.",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="expose", description="expose a user...")
    @app_commands.describe(user="user to expose")
    async def expose(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user

        exposes = [
            f"**{user.name}** tried to download more RAM and got scared when it worked",
            f"**{user.name}** blinked manually and forgot how to stop",
            f"**{user.name}** lost a 1v1 against their own thoughts",
            f"**{user.name}** got banned from a singleplayer game",
            f"**{user.name}** unplugged something to charge it faster",
            f"**{user.name}** failed a tutorial level and blamed the devs",
            f"**{user.name}** tried to scroll on a screenshot",
            f"**{user.name}** heard a noise at night and accepted their fate instantly",
            f"**{user.name}** tried to skip an unskippable cutscene in real life",
            f"**{user.name}** got jump scared by their own reflection",
            f"**{user.name}** installed confidence.exe and it crashed",
            f"**{user.name}** opened task manager and got nervous",
            f"**{user.name}** thought 'AFK' was a country",
            f"**{user.name}** paused the microwave at 1 second like they just defused a bomb",
            f"**{user.name}** breathed too manually and had to restart",
            f"**{user.name}** tried to ctrl+z a real life decision",
        ]

        embed = discord.Embed(
            title="Expose Time! 🕵️‍♂️",
            description=random.choice(exposes),
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Exposed by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="compliment", description="give someone a compliment :3")
    @app_commands.describe(user="user to compliment")
    async def compliment(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user

        compliments = [
            f"**{user.name}** is a wonderful person!",
            f"**{user.name}** has a great sense of humor!",
            f"**{user.name}** is incredibly kind!",
            f"**{user.name}** makes the world a better place!",
            f"**{user.name}** is very talented!",
            f"**{user.name}** is very smart!",
            f"**{user.name}** is awesome 😎",
            f"**{user.name}** is built different (in a good way)",
            f"**{user.name}** has main character energy",
            f"**{user.name}** is a W human",
            f"**{user.name}** deserves a snack right now",
        ]

        embed = discord.Embed(
            title="Compliment Time! 💖",
            description=random.choice(compliments),
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Complimented by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="roast", description="roast someone :3")
    @app_commands.describe(user="user to roast")
    async def roast(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user

        roasts = [
            f"**{user.name}** is running on 2 braincells and they’re both buffering",
            f"**{user.name}** has the confidence of someone who is completely wrong",
            f"**{user.name}** would lose a staring contest with a wall",
            f"**{user.name}** looks like they say 'huh' after understanding everything",
            f"**{user.name}** has negative ping in real life",
            f"**{user.name}** presses 'try again' like it’s a personality trait",
            f"**{user.name}** got early access to making bad decisions",
            f"**{user.name}** would get lost in a straight line",
            f"**{user.name}** is the reason tutorials have step 1",
            f"**{user.name}** thought the floor was optional",
        ]

        embed = discord.Embed(
            title="Roast Time! 🔥",
            description=random.choice(roasts),
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Roasted by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="slap", description="slap someone lol")
    async def slap(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(
            title="Slap 💥",
            description=f"**{user.name}** got slapped with a force of **{random.randint(1, 100)}%**!",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Slapped by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="hug", description="hug someone <3")
    async def hug(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(
            title="Hug 🫂",
            description=f"**{user.name}** got hugged with a force of **{random.randint(1, 100)}%**!",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Hugged by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="poke", description="poke someone hehe")
    async def poke(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(
            title="Poke 👉",
            description=f"**{user.name}** got poked with a force of **{random.randint(1, 100)}%**!",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Poked by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="highfive", description="high five someone!")
    async def highfive(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(
            title="High Five 👏",
            description=f"**{user.name}** got high fived with a force of **{random.randint(1, 100)}%**!",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"High Fived by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="rate", description="use our very accurate rating system!!1!!")
    async def rate(self, interaction: Interaction, thing: str):
        rating = random.randint(1, 10)

        embed = discord.Embed(
            title="Rating ⭐",
            description=f"I rate **{thing}** a **{rating}/10**!",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="nominate", description="this user is most likely to...")
    async def nominate(self, interaction: Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user

        nominations = [
            f"**{user.name}** is most likely to trip over nothing in public",
            f"**{user.name}** is most likely to forget what they were saying mid sentence",
            f"**{user.name}** is most likely to laugh at the wrong moment",
            f"**{user.name}** is most likely to open the fridge and stare into the void",
            f"**{user.name}** is most likely to send a message and instantly regret it",
            f"**{user.name}** is most likely to fall asleep at the worst possible time",
            f"**{user.name}** is most likely to vibe to music no one else hears",
            f"**{user.name}** is most likely to press the wrong button every time",
        ]

        embed = discord.Embed(
            title="You have been nominated! 🫡",
            description=random.choice(nominations),
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Nominated by {interaction.user.name} • Clanker")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Social(bot))
    