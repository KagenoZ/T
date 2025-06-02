import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

keep_alive()  # This will start the web server


# Bot prefix and intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Echo command
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Add command
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f"The sum is: {a + b}")

load_dotenv()
bot.run(os.getenv('TOKEN'))



