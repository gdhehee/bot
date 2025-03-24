import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="info", description="Shows bot information and commands")
    async def info(self, ctx):
        embed = discord.Embed(title="Ultimate Bot", description="Developed by Hacker", color=discord.Color.blue())
        embed.add_field(name="User Commands", value="""
        - !meme
        - !joke
        - !8ball [question]
        - !roast @user
        - !riddle
        - !fun commands...
        """, inline=False)
        embed.add_field(name="Moderator Commands", value="""
        - !ban @user [reason]
        - !kick @user [reason]
        - !warn @user
        - !purge [amount]
        - !fakeban @user
        """, inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
