import discord
from discord.ext import commands

class MagicConch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='magic_conch')
    async def magic_conch(self, ctx):
        await ctx.send("Magic Conch 기능 실행")

# Cog를 추가
async def setup(bot):
    await bot.add_cog(MagicConch(bot))
