import discord
import os
import random
import platform

from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN') # 봇 토큰 
guild_id_raw = os.getenv('GUILD_ID') # 서버 ID

if ',' in guild_id_raw:
    GUILD_ID = list(map(int, guild_id_raw.split(',')))
else:
    GUILD_ID = [int(guild_id_raw)] 


intents = discord.Intents.default()
intents.members = True 
intents.message_content = True


class GachaBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix='/',
            intents=intents,
            help_command=commands.DefaultHelpCommand(),
        )
    
    async def load_cogs(self) -> None:
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                    print(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    print(
                        f"Failed to load extension {extension}\n{exception}"
                    )

    # 봇 상태 무작위 변경 (game status task)
    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:
        statuses = ["ㅇㅇ", "를!", "나가"]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

    # 봇 시작 전까지 상태 변경 대기 
    @status_task.before_loop
    async def before_status_task(self) -> None:
        await self.wait_until_ready()
    
    async def setup_hook(self) -> None:
        print(f"Logged in as {self.user.name}")
        print(f"discord.py API version: {discord.__version__}")
        print(f"Python version: {platform.python_version()}")
        print(
            f"Running on: {platform.system()} {platform.release()} ({os.name})"
        )
        print("-------------------")

        await self.load_cogs()
        self.status_task.start()

        # 슬래시 명령어 동기화
        for guild_id in GUILD_ID:
            guild = discord.Object(id=guild_id)
            try:
                await self.tree.sync(guild=guild)
                print(f"Commands synced for guild {guild_id}.")
            except Exception as e:
                print(f"Failed to sync commands for guild {guild_id}: {e}")


bot = GachaBot()
bot.run(TOKEN)