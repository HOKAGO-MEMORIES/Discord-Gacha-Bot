import discord
from discord import Game, Status
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN') # 봇 토큰 
GUILD_ID = int(os.getenv('GUILD_ID')) # 서버 ID

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True

current_user = None # 현재 봇을 사용하고 있는 사람
        
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))

client = MyClient(intents=intents)
        
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
    game = Game("ㅇㅇ")
    await client.change_presence(status=Status.online, activity=game)
    

# Cog 로드
async def load_extensions():
    await client.load_extension('cogs.vote')
    await client.load_extension('cogs.team')
    await client.load_extension('cogs.magic_conch')
    

client.run(TOKEN)