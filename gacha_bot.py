# 메인 함수
import discord
import os
from discord.ext import commands
# 토큰 불러오기
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('Token')

bot = commands.Bot(command_prefix='/')

# 콘솔
@bot.event
async def on_ready():
    print('=============================')
    print('Logged in as')
    print(f'USERNAME : {bot.user.name}')
    print(f'  I   D  : {bot.user.id}')
    print('=============================')

bot.run(token)