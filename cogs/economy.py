import discord
from discord.ext import commands
import random
from database.db import get_db

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        # Dummy implementation
        await ctx.send(f"💰 {ctx.author.mention} your balance is 100 coins.")

    @commands.command()
    async def work(self, ctx):
        coins = random.randint(10, 50)
        await ctx.send(f"💼 {ctx.author.mention} you worked and earned {coins} coins!")

    @commands.command()
    async def gamble(self, ctx, amount: int):
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            await ctx.send(f"🎉 {ctx.author.mention} you gambled and won {amount*2} coins!")
        else:
            await ctx.send(f"😢 {ctx.author.mention} you gambled and lost {amount} coins.")

def setup(bot):
    bot.add_cog(Economy(bot))
