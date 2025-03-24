import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.ban(reason=reason)
        await ctx.send(f"🚫 {member.mention} has been banned for: {reason}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member.mention} has been kicked for: {reason}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"🧹 Purged {amount} messages.", delete_after=3)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def fakeban(self, ctx, member: discord.Member):
        # Fake ban (prank command)
        await ctx.send(f"🚫 {member.mention} has been *fake banned*. Just kidding!")
        
def setup(bot):
    bot.add_cog(Moderation(bot))
