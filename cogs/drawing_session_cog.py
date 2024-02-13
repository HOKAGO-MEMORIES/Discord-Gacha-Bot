# 기본적인 흐름과 상호작용에 대한 전반적인 로직
from discord.ext import commands, ui
from utils.drawbuttion import DrawButton
from utils.options import option_1, option_2, option_3

class DrawingSessionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.in_use = False  # 현재 이용 여부를 나타내는 변수
   
    # /start 명령어
    @commands.slash_command(name='start', description='명령어 사용')
    async def start(self, ctx):
        if self.in_use:
            await ctx.send('다른 사람이 현재 사용중입니다! 끝날 때까지 기다려주세요...')
            return
    
        self.in_use = True
    
        view = ui.View()
        
        view.add_item(DrawButton(ctx, view, label='1번', custom_id='draw_button_1', callback=None))
        view.add_item(DrawButton(ctx, view, label='2번', custom_id='draw_button_2', callback=None))
        view.add_item(DrawButton(ctx, view, label='3번', custom_id='draw_button_3', callback=None))  
          
        await ctx.send("버튼을 눌러주세요! \n1번 : 여러 키워드 입력 후 하나 추첨 \n2번 : 유저 중에서 당첨자 추첨 \n3번 : 마법의 소라고동", view=view)