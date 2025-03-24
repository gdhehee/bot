import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

TOKEN = os.getenv("TOKEN")
COMMAND_PREFIX = "!"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Load all cogs from the cogs folder
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")
    await bot.change_presence(activity=discord.Game(name="UltimateBot Active"))

bot.run(TOKEN)
