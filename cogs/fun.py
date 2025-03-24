import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        await ctx.send("😂 Here's a meme! (Feature pending implementation)")

    @commands.command()
    async def joke(self, ctx):
        jokes = ["Why don't scientists trust atoms? Because they make up everything!", 
                 "Why did the chicken cross the road? To get to the other side!"]
        await ctx.send(random.choice(jokes))

    @commands.command()
    async def roast(self, ctx, member: discord.Member):
        roasts = ["You're as useless as the 'ueue' in 'queue'.", "I'd agree with you, but then we'd both be wrong."]
        await ctx.send(f"{member.mention}, {random.choice(roasts)}")

    @commands.command(name="8ball")
    async def eightball(self, ctx, *, question: str):
        responses = ["It is certain.", "Ask again later.", "Very doubtful."]
        await ctx.send(f"🎱 {random.choice(responses)}")

    @commands.command()
    async def riddle(self, ctx):
        riddles = [
            ("I speak without a mouth and hear without ears. What am I?", "An echo"),
            ("What has keys but can't open locks?", "A piano")
        ]
        riddle, answer = random.choice(riddles)
        await ctx.send(f"❓ Riddle: {riddle}\n*(Answer: {answer})*")
        
    # More fun commands can be added similarly.
    
def setup(bot):
    bot.add_cog(Fun(bot))
