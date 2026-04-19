# im a manipwuation file

from discord import app_commands, Interaction
from discord.ext import commands
import discord
import aiohttp
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import io

class Manipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="manipulation", description="See what the manipulation category does")
    async def manipulation(self, interaction: Interaction):
        command_count = len(self.get_app_commands())
        embed = discord.Embed(
            title="Manipulation 📚",
            description=(
                "Hello, the manipulation category handles all of the image manipulation commands!\n"
                f"There are currently **{command_count} commands** in this category."
            ),
            color=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)

    async def get_image(self, interaction: Interaction, image: discord.Attachment = None, url: str = None):
        image_url = None

        if image:
            image_url = image.url
        elif url:
            image_url = url
        elif interaction.message and interaction.message.reference:
            try:
                replied = await interaction.channel.fetch_message(interaction.message.reference.message_id)
                if replied.attachments:
                    image_url = replied.attachments[0].url
            except:
                pass
        if not image_url:
            async for msg in interaction.channel.history(limit=20):
                if msg.attachments:
                    image_url = msg.attachments[0].url
                    break

        if not image_url:
            return None, "Missing Image ⚠️", "Upload, reply, or provide a URL."

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    if resp.status != 200:
                        return None, "Error 🚫", "Failed to download the image."
                    data = await resp.read()
            return Image.open(io.BytesIO(data)), None, None
        except:
            return None, "Error 🚫", "Invalid image format."

    async def send_error(self, interaction: Interaction, title: str, desc: str):
        embed = discord.Embed(
            title=title,
            description=desc,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    async def send_image(self, interaction: Interaction, img: Image.Image, title: str, filename: str, desc: str = None):
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        file = discord.File(buffer, filename=filename)
        embed = discord.Embed(
            title=title,
            description=desc if desc else "",
            color=discord.Color.blurple()
        )
        embed.set_image(url=f"attachment://{filename}")
        await interaction.response.send_message(embed=embed, file=file)

    @app_commands.command(name="invert", description="Invert an image")
    async def invert(self, interaction: Interaction, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = ImageOps.invert(img.convert("RGB"))
        await self.send_image(interaction, img, "Inverted Image 🌀", "invert.png")

    @app_commands.command(name="greyscale", description="Convert image to greyscale")
    async def greyscale(self, interaction: Interaction, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = ImageOps.grayscale(img)
        await self.send_image(interaction, img, "Greyscale Image ⚪", "greyscale.png")

    @app_commands.command(name="deepfry", description="Deep fry an image")
    async def deepfry(self, interaction: Interaction, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = img.convert("RGB")
        img = ImageEnhance.Contrast(img).enhance(2.0)
        img = ImageEnhance.Color(img).enhance(3.0)
        img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
        await self.send_image(interaction, img, "Deepfried Image 💥", "deepfry.png")

    @app_commands.command(name="blur", description="Blur an image")
    async def blur(self, interaction: Interaction, amount: int = 5, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = img.filter(ImageFilter.GaussianBlur(radius=amount))
        await self.send_image(interaction, img, f"Blurred Image (Amount: {amount}) 💨", "blur.png")

    @app_commands.command(name="bloom", description="Add bloom effect")
    async def bloom(self, interaction: Interaction, amount: float = 1.5, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = ImageEnhance.Brightness(img).enhance(amount)
        img = img.filter(ImageFilter.GaussianBlur(radius=5))
        await self.send_image(interaction, img, f"Bloom Image (Amount: {amount}) ✨", "bloom.png")

    @app_commands.command(name="pixelate", description="Pixelate an image")
    async def pixelate(self, interaction: Interaction, amount: int = 10, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = img.resize((img.width // amount, img.height // amount), Image.NEAREST)
        img = img.resize((img.width * amount, img.height * amount), Image.NEAREST)
        await self.send_image(interaction, img, f"Pixelated Image (Amount: {amount}) 🟫", "pixelate.png")

    @app_commands.command(name="gif", description="Turn an image into a GIF")
    async def gif(self, interaction: Interaction, image: discord.Attachment = None, url: str = None):
        img, err_title, err_desc = await self.get_image(interaction, image, url)
        if not img:
            return await self.send_error(interaction, err_title, err_desc)
        img = img.convert("RGBA")
        buffer = io.BytesIO()
        img.save(buffer, format="GIF", save_all=True, loop=0)
        buffer.seek(0)
        file = discord.File(buffer, filename="image.gif")
        embed = discord.Embed(
            title="Image → GIF 🖼️",
            description="GIFs are limited to 256 colors - quality may drop ⚠️",
            color=discord.Color.blurple()
        )
        embed.set_image(url="attachment://image.gif")
        await interaction.response.send_message(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Manipulation(bot))
    