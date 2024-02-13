# 메인 함수
import os
from discord.ext import commands
from discord import Intents
# 토큰 불러오기
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('Token')

intents = Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# 콘솔
@bot.event
async def on_ready():
    print('=============================')
    print('Logged in as')
    print(f'USERNAME : {bot.user.name}')
    print(f'  I   D  : {bot.user.id}')
    print('=============================')

bot.load_extension('drawing_session_cog')

bot.run(token)