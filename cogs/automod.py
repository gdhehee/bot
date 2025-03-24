import discord
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bad_words = ["badword1", "badword2"]
        self.link_blacklist = ["http://", "https://"]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # Auto-Delete Links
        if any(link in message.content for link in self.link_blacklist):
            try:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, links are not allowed!")
            except:
                pass

        # Blacklist system for bad words
        if any(word in message.content.lower() for word in self.bad_words):
            try:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, watch your language!")
            except:
                pass

        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(AutoMod(bot))
