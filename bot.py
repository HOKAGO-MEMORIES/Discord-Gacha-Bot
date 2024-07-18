import discord
from discord import Game, Status
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN') # 봇 토큰 
GUILD_ID = int(os.getenv('GUILD_ID')) # 서버 ID

intents = discord.Intents.default()

current_user = None # 현재 봇을 사용하고 있는 사람

bot = commands.Bot(command_prefix='!', intents=intents)
        
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    game = Game("ㅇㅇ")
    await bot.change_presence(status=Status.online, activity=game)

bot.load_extension('cogs.vote')
bot.load_extension('cogs.team')
bot.load_extension('cogs.magic_conch')

bot.run(TOKEN)