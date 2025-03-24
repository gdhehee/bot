import discord
from discord.ext import commands
from database.db import get_db

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_verification(self, ctx, channel: discord.TextChannel, role: discord.Role):
        msg = await channel.send("✅ React with ✅ to verify!")
        await msg.add_reaction("✅")
        # Store verification message, channel, and role info in database or a file
        await ctx.send(f"Verification setup complete in {channel.mention} with role {role.mention}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if str(payload.emoji) != "✅":
            return
        # Check if it's the verification message (implement your storage logic)
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        # For simplicity, assume it's the verification message
        verified_role = discord.utils.get(guild.roles, name="Verified")
        if verified_role and member:
            await member.add_roles(verified_role)
            try:
                await member.send("🎉 You are now verified!")
            except:
                pass

def setup(bot):
    bot.add_cog(Verification(bot))
