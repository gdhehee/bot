
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

TOKEN = os.getenv("TOKEN")
COMMAND_PREFIX = "!"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Detect Render port for web service (if necessary)
port = int(os.environ.get("PORT", 10000))  # Default to 10000 if no port is found

# Load all cogs from the cogs folder
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")
    await bot.change_presence(activity=discord.Game(name="UltimateBot Active"))

# Start the bot as usual (Web service won't be needed unless you have a web server in the bot)
bot.run(TOKEN)
