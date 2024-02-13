import discord
import os

from discord.ext import commands, ui

# 토큰 불러오기
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('Token')

bot = commands.Bot(command_prefix='/')


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
    
        # 여러 키워드 입력 후 하나 추첨
        option_1 = ui.Button(label='1번', custom_id='draw_button_1')
        # 유저 중에서 당첨자 추첨
        option_2 = ui.Button(label='2번', custom_id='draw_button_2')
    
        view = ui.View()
        view.add_item(option_1)
        view.add_item(option_2)
    
        await ctx.send("버튼을 눌러주세요! \n1번 : 여러 키워드 입력 후 하나 추첨 \n2번 : 유저 중에서 당첨자 추첨", view=view)
    
        @option_1.callback
        async def on_option_1_click(interaction):
            # 1번 버튼을 눌렀을 경우

            await interaction.response.send_message()
    
        @option_2.callback
        async def on_option_2_click(interaction):
            # 2번 버튼을 눌렀을 경우

            await interaction.response.send_message()
          

# 콘솔
@bot.event
async def on_ready():
    print('=============================')
    print('Logged in as')
    print(f'USERNAME : {bot.user.name}')
    print(f'  I   D  : {bot.user.id}')
    print('=============================')


bot.run(token)