import discord
from discord.ext import commands
import asyncio

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_ticket(self, ctx, channel: discord.TextChannel):
        msg = await channel.send("🎫 React with 🎫 to open a ticket!")
        await msg.add_reaction("🎫")
        await ctx.send("Ticket system setup complete.")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if str(payload.emoji) != "🎫":
            return
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        category = discord.utils.get(guild.categories, name="Tickets")
        if not category:
            category = await guild.create_category("Tickets")
        ticket_channel = await guild.create_text_channel(f"ticket-{member.name}", category=category)
        await ticket_channel.set_permissions(member, read_messages=True, send_messages=True)
        await ticket_channel.set_permissions(guild.default_role, read_messages=False)
        await ticket_channel.send(f"{member.mention} opened a ticket. Use `!close` to close this ticket.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def close(self, ctx):
        if "ticket-" in ctx.channel.name:
            await ctx.send("Closing ticket in 5 seconds...")
            await asyncio.sleep(5)
            await ctx.channel.delete()

def setup(bot):
    bot.add_cog(Tickets(bot))
