import discord
from discord.ext import commands
from database.db import get_db

class Rewards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setreward(self, ctx, role: discord.Role, invites_needed: int):
        # For simplicity, store in a text file or SQLite table
        conn, cursor = get_db()
        cursor.execute("CREATE TABLE IF NOT EXISTS rewards (guild_id INTEGER, role_id INTEGER, invites_needed INTEGER)")
        cursor.execute("INSERT OR REPLACE INTO rewards (guild_id, role_id, invites_needed) VALUES (?, ?, ?)", (ctx.guild.id, role.id, invites_needed))
        conn.commit()
        await ctx.send(f"🏆 Reward role {role.mention} set for users with {invites_needed} invites!")

def setup(bot):
    bot.add_cog(Rewards(bot))
