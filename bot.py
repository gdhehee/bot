
import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import asyncio

load_dotenv()  # Loads .env file

TOKEN = os.getenv("TOKEN")
COMMAND_PREFIX = "!"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Create Flask app for web service
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# This function will allow the bot to run with Flask in the same process
async def run_flask():
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if no port is found
    app.run(host="0.0.0.0", port=port)

# Load all cogs from the cogs folder with error handling and await the load_extension
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

# Override setup_hook to load cogs before the bot starts running
async def setup():
    await load_cogs()

bot.setup_hook = setup

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")
    await bot.change_presence(activity=discord.Game(name="UltimateBot Active"))

# Start Flask in a separate thread to prevent blocking
thread = Thread(target=lambda: asyncio.run(run_flask()))
thread.start()

# Start the bot as usual
bot.run(TOKEN)
