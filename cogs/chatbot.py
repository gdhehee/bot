import discord
from discord.ext import commands

class ChatBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chat_channel_id = None  # Set via a command

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setchat(self, ctx, channel: discord.TextChannel):
        self.chat_channel_id = channel.id
        await ctx.send(f"🤖 ChatBot mode enabled in {channel.mention}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if self.chat_channel_id and message.channel.id == self.chat_channel_id:
            # Simple echo chatbot for demonstration. Replace with an AI API if needed.
            await message.channel.send(f"You said: {message.content}")
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(ChatBot(bot))
