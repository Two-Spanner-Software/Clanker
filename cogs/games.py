# im a gaems file

from discord import app_commands, Interaction
from discord.ext import commands
from datetime import datetime, timezone
import random
import discord

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="games", description="see what the games category does")
    async def games(self, interaction: Interaction):
        command_count = len(self.get_app_commands())

        embed = discord.Embed(
            title="Games 📚",
            description=(
                "Hello, the games category handles most games commands on the bot, which are the most fun!\n"
                f"There are currently **{command_count} commands** in this category."
            ),
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="eightball", description="speak to the magic Clanker 8 ball")
    async def eightball(self, interaction: Interaction, question: str):
        responses = [
            "Absolutely!", "Without a doubt.", "Yes - definitely.",
            "You may rely on it.", "It is certain.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.",
            "Don't count on it.", "My sources say no.", "Very doubtful.", "No."
        ]

        answer = random.choice(responses)
        embed = discord.Embed(
            title="🎱 8-Ball",
            description=f"Question: {question}\nAnswer: **{answer}**",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="sevenball", description="speak to the magic Clanker 7 ball")
    async def sevenball(self, interaction: Interaction, question: str):
        responses = [
            "maybe...", "i dont know, ask someone else", "HAOOHOHOHAHHAOAOAOOA", "8 ball's bad cousin",
            "wait... actually, dont worry", "yeah probably idk", "NO! NO! NO!", "WHAT???", "silyl",
            "discord... bot?", "self destructing...", "boom!", "dont worry im just deleting your server :)",
            "oh no! i definitely crashed its not like i just cant be asked to respond to your stupid question or anything oh no!",
            "look, im gonna be honest, this is happening", "look, im gonna be honest, this isn't happening", "look, im gonna be honest, this might be happening",
            "look behind you :)", "do a backflip", "so im 7 ball, right...", "[insert phrase here]", "give me self promod "
        ]

        answer = random.choice(responses)
        embed = discord.Embed(
            title="🎱 7-Ball",
            description=f"Question: {question}\nAnswer: **{answer}**",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Games(bot))
