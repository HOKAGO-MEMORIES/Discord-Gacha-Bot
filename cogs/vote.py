import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vote')
    async def vote(self, ctx):
        global current_vote_user
        if current_vote_user is None:
            current_vote_user = ctx.author.id
            try:
                await ctx.send("Vote 기능 실행 중")
                # 투표 기능 로직을 여기에 추가
            finally:
                current_vote_user = None  # 기능 완료 후 초기화
        else:
            await ctx.send(f'{ctx.author.mention}, 현재 다른 사용자가 vote 기능을 사용 중입니다. 잠시 후 다시 시도해 주세요.')

# Cog를 추가
async def setup(bot):
    await bot.add_cog(Vote(bot))
