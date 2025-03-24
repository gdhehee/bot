import discord
from discord.ext import commands
from database.db import get_db

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason provided"):
        conn, cursor = get_db()
        cursor.execute("SELECT count FROM warnings WHERE user_id=? AND guild_id=?", (member.id, ctx.guild.id))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO warnings (user_id, guild_id, count) VALUES (?, ?, ?)", (member.id, ctx.guild.id, 1))
        else:
            cursor.execute("UPDATE warnings SET count = count + 1 WHERE user_id=? AND guild_id=?", (member.id, ctx.guild.id))
        conn.commit()
        await ctx.send(f"⚠️ {member.mention} has been warned.")
        
    @commands.command()
    async def warnings(self, ctx, member: discord.Member):
        conn, cursor = get_db()
        cursor.execute("SELECT count FROM warnings WHERE user_id=? AND guild_id=?", (member.id, ctx.guild.id))
        data = cursor.fetchone()
        count = data[0] if data else 0
        await ctx.send(f"⚠️ {member.mention} has {count} warnings.")

def setup(bot):
    bot.add_cog(Warnings(bot))
