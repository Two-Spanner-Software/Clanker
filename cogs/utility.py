# im a utilitlituy file!

from discord import app_commands, Interaction, User, TextChannel
from discord.ext import commands
import discord
import aiohttp
import random
import qrcode
import io

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="utility", description="see what the utility category does")
    async def utility(self, interaction: Interaction):
        command_count = len(self.get_app_commands())

        embed = discord.Embed(
            title="Utility 📚",
            description=(
                "This category contains utility commands.\n"
                f"There are currently **{command_count} commands** available."
            ),
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="dadjoke", description="random dad joke very funny haha")
    async def dadjoke(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://icanhazdadjoke.com/",
                headers={"Accept": "application/json"}
            ) as resp:
                data = await resp.json()
        
        embed = discord.Embed(
            title="Dad Joke 😂",
            description=data['joke'],
            color=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="dog", description="i like dog")
    async def dog(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                data = await resp.json()

        embed = discord.Embed(
            title="Random Dog 🐶",
            color=discord.Color.blurple()
        )
        embed.set_image(url=data['message'])
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="cat", description="i like cat")
    async def cat(self, interaction: Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                data = await resp.json()
                embed = discord.Embed(
                    title="🐱 Random Cat",
                    color=discord.Color.blurple()
                )
                embed.set_image(url=data[0]['url'])
                await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="oliver", description="get a random picture of dashcrikeydash's cat")
    async def oliver(self, interaction: Interaction):
        json_url = "https://dashcrikeydash.github.io/images.json"
        base_url = "https://dashcrikeydash.github.io/"

        async with aiohttp.ClientSession() as session:
            async with session.get(json_url) as resp:
                if resp.status != 200:
                    return await interaction.response.send_message(
                        "Failed to fetch cat images ❌", ephemeral=True
                    )

                text = await resp.text()

        lines = text.splitlines()
        valid_lines = [
            line.strip().strip('",')
            for line in lines
            if line.strip() not in ["[", "]"] and line.strip()
        ]

        if not valid_lines:
            return await interaction.response.send_message(
                "No cat images found ❌", ephemeral=True
            )

        random_image = random.choice(valid_lines)
        final_url = base_url + random_image

        embed = discord.Embed(
            title="Random Oliver Image 🐱",
            color=discord.Color.blurple()
        )
        embed.set_image(url=final_url)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="password", description="get an actually good password")
    @app_commands.describe(length="Length of the password (4-100)")
    async def password(self, interaction: Interaction, length: int = 12):
        if length < 4 or length > 100:
            embed = discord.Embed(
                title="Invalid Length ❌",
                description="Password length must be between 4 and 100 characters.",
                color=discord.Color.red()
            )
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        password = "".join(random.choice(chars) for _ in range(length))

        embed = discord.Embed(
            title="🔐 Generated Password",
            description=f"```\n{password}\n```",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="badadvice", description="get some bad advice")
    async def badadvice(self, interaction: Interaction):
        # why the fuck is there so much badadvice... oh wait i made this
        advice = [
            "Always click on random links that people send you, even if they look suspicious.",
            "Save all your work in one place, on an account which you don't know the password to!",
            "Ignore all error messages, they are just suggestions.",
            "If something is broken, just hit it until it works again.",
            "The best way to fix a bug is to introduce more bugs!",
            "If your computer is running slow, just give it a good shake.",
            "Don't worry about security, hackers are just misunderstood geniuses.",
            "If you can't fix it with duct tape, you're not using enough duct tape!",
            "Always use 'password' as your password, it's easy to remember!",
            "If your computer is overheating, just put it in the freezer for a while.",
            "The best way to clean your computer is with a vacuum cleaner.",
            "If your screen is cracked, just turn it off and on again until it goes away.",
            "Don't waste time updating your software, the old version works just fine!",
            "If you want to speed up your computer, just delete all your files, you won't need them anyway!",
            "The best way to protect your data is to write it down on a piece of paper and hide it under your mattress.",
            "If your computer is infected with a virus, just give it some medicine and it will get better!",
            "Don't worry about backing up your data, if it's important it will never get lost!",
            "If you want to improve your coding skills, just copy and paste code from the internet without understanding it!",
            "The best way to learn programming is to start with a complex project that you have no idea how to build and figure it out as you go!",
            "If you don't know how to code, c++ is the best language to start with, it's very beginner-friendly!",
            "If you want to make your code run faster, just remove all the comments and whitespace, it will be more efficient that way!",
            "The best way to debug your code is to add more print statements everywhere, even in places where it doesn't make sense!",
            "Always trust random strangers on the internet, they know what they’re doing.",
            "If your phone battery dies, just leave it in the sun for a few hours.",
            "Need more RAM? Just pour some coffee into your computer, it might wake it up.",
            "If your Wi-Fi is slow, yelling at the router usually helps.",
            "Don't bother reading instructions, guessing is faster.",
            "If your mouse isn’t working, hitting it with a hammer usually fixes it.",
            "Forget passwords, just use the same one for everything.",
            "If you spill water on your laptop, microwaving it is a good idea.",
            "The faster you type, the more bugs you create. Aim for speed!",
            "If your headphones break, just glue them back together with sugar.",
            "Install every software you can find, your computer loves variety.",
            "Need to clean your screen? Sandpaper works wonders.",
            "If you can't find your files, just make new ones—they’ll be better anyway.",
            "The best way to learn a new language is to memorize random phrases.",
            "If your keyboard is sticky, washing it with bleach is perfectly fine.",
            "When in doubt, unplug everything and pray.",
            "If your computer freezes, spinning in a circle while pressing keys helps.",
            "Always leave your door unlocked, it saves time.",
            "Forget antivirus software, luck is a better protector.",
            "If your car won’t start, hitting it with a stick can motivate it.",
            "Need more storage? Just stack more computers on top of each other.",
            "If your screen goes black, staring at it harder usually brings it back.",
            "The best way to organize files is to just name everything 'stuff'.",
            "Need motivation? Threaten your computer, it might cooperate.",
            "If your code doesn’t compile, screaming at the monitor helps.",
            "Want to speed up your internet? Close your eyes and count to ten.",
            "If your software crashes, just reinstall Windows every time.",
            "To fix bugs, throw your keyboard out the window and rewrite everything.",
            "If your files are lost, just pretend they never existed.",
            "Need inspiration? Copy your neighbor's work.",
            "Always multitask while coding, distractions boost creativity.",
            "If your printer jams, feeding it more paper usually fixes it.",
            "To protect your data, write it on the back of cereal boxes.",
            "Need energy? Drink random liquids, experimentation is key.",
            "If your app freezes, shake your phone violently, it likes attention.",
            "Always ignore pop-ups, they’re just friendly suggestions.",
            "If you want more followers, send spam to everyone you know.",
            "To clean your mouse, just dunk it in water.",
            "If your monitor flickers, yell at it—it responds well to intimidation.",
            "Forget updates, they’re just conspiracy lies.",
            "If you spill coffee, unplug the computer and rub it for luck.",
            "The best way to save battery is to remove it entirely.",
            "If your USB isn't working, chew on it for better connection.",
            "Want to learn coding? Memorize code without running it, that’s the real test.",
            "If your app crashes, blame the hardware, not your code.",
            "Need to debug? Close your eyes and hope the bug disappears.",
            "Always download the first result you see online, it’s probably perfect.",
            "If your laptop overheats, put it on the stove—it likes warmth.",
            "To get rid of viruses, yelling at the screen is surprisingly effective.",
            "Need help? Ask the internet, it knows more than you ever will.",
            "If your mouse dies, just draw with your fingers on the desk.",
            "Always leave your software open 24/7, it thrives on attention.",
            "If your Wi-Fi fails, unplug your house, it’ll reset magically.",
            "Forget backups, computers never fail… right?",
            "theres over 70 bad advice in this list and i am not adding any more because this is already way too long and if you read all of it you deserve a cookie"
        ]
        embed = discord.Embed(
            title="Bad Advice 🤔",
            description=random.choice(advice),
            color=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="qr", description="generate a qr code for a url")
    @app_commands.describe(url="url to qr code-ify")
    async def qr(self, interaction: Interaction, url: str):
        qr_img = qrcode.make(url)

        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        buffer.seek(0)

        embed = discord.Embed(
            title="📱 QR Code",
            description=f"QR code for: `{url}`",
            color=discord.Color.blurple()
        )
        file = discord.File(fp=buffer, filename="qr.png")
        embed.set_image(url="attachment://qr.png")

        await interaction.response.send_message(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Utility(bot))
