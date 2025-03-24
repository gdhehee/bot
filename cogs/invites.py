import discord
from discord.ext import commands
from database.db import get_db

class Invites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invites(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        conn, cursor = get_db()
        cursor.execute("SELECT count FROM invites WHERE user_id=? AND guild_id=?", (member.id, ctx.guild.id))
        result = cursor.fetchone()
        count = result[0] if result else 0
        await ctx.send(f"📨 {member.mention} has invited {count} members.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def resetinvites(self, ctx, member: discord.Member):
        conn, cursor = get_db()
        cursor.execute("UPDATE invites SET count=0 WHERE user_id=? AND guild_id=?", (member.id, ctx.guild.id))
        conn.commit()
        await ctx.send(f"🔄 {member.mention}'s invite count has been reset.")

def setup(bot):
    bot.add_cog(Invites(bot))
