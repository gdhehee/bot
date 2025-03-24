import discord
from discord.ext import commands, tasks
import asyncio
import random

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def gcreate(self, ctx, duration: int, winners: int, *, prize: str):
        msg = await ctx.send(f"🎉 Giveaway for **{prize}**! Ends in {duration} seconds. React with 🎉 to enter!")
        await msg.add_reaction("🎉")
        await asyncio.sleep(duration)
        msg = await ctx.channel.fetch_message(msg.id)
        users = [user for reaction in msg.reactions for user in await reaction.users().flatten() if not user.bot]
        if users:
            winner_list = random.sample(users, min(winners, len(users)))
            winners_str = ", ".join(user.mention for user in winner_list)
            await ctx.send(f"🏆 Congratulations {winners_str}! You won **{prize}**!")
        else:
            await ctx.send("No entries were received.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def greroll(self, ctx, message_id: int):
        msg = await ctx.channel.fetch_message(message_id)
        users = [user for reaction in msg.reactions for user in await reaction.users().flatten() if not user.bot]
        if users:
            winner = random.choice(users)
            await ctx.send(f"🔄 New winner: {winner.mention}")
        else:
            await ctx.send("No entries were found.")

def setup(bot):
    bot.add_cog(Giveaways(bot))
