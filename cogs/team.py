import discord
from discord.ext import commands

class Team(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='team')
    async def team(self, ctx):
        global current_user
        if current_user is None:
            current_user = ctx.author.id
            try:
                await ctx.send("Team 기능 실행 중")
                # 팀 기능 로직을 여기에 추가
            finally:
                current_user = None  # 기능 완료 후 초기화
        else:
            await ctx.send(f'{ctx.author.mention}, 현재 다른 사용자가 team 기능을 사용 중입니다. 잠시 후 다시 시도해 주세요.')

# Cog를 추가
async def setup(bot):
    await bot.add_cog(Team(bot))
