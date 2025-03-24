import discord
from discord.ext import commands

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}

    @commands.command()
    async def afk(self, ctx, *, reason="AFK"):
        self.afk_users[ctx.author.id] = reason
        await ctx.send(f"{ctx.author.mention} is now AFK: {reason}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        for user_id in list(self.afk_users.keys()):
            if str(user_id) in [str(member.id) for member in message.mentions]:
                await message.channel.send(f"<@{user_id}> is AFK: {self.afk_users[user_id]}")
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(AFK(bot))
