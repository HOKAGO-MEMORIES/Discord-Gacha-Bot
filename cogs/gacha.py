import random
import discord
import asyncio

from discord import app_commands
from discord.ext import commands
from typing import Literal

class Gacha(commands.Cog, name="gacha"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="가챠",
        description="선택하기 힘들 때 무작위로 뽑아봅시다."
    )
    @app_commands.describe(
        type="1: 혼자 모든 항목을 작성합니다.  /  2: 현재 음성채널에 함께 있는 모든 사람과 항목을 작성합니다.  /  3: 모두가 항목을 작성합니다.",
    )
    async def gacha(self, interaction: discord.Interaction, type: Literal[1, 2, 3]) -> None:
        if type == 1:
            await self.gacha_single(interaction)
        elif type == 2:
            await self.gacha_voice_channel(interaction)
        elif type == 3:
            await self.gacha_multiple(interaction)

    # type: 1
    async def gacha_single(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            "항목을 별도의 메시지로 작성해 주세요. ex) 바나나, 사과, 오렌지를 각각의 메시지로 입력합니다. \n"
            "제한 시간은 60초 입니다. 입력 완료 후 '완료!'라고 입력해 주세요."
        )

        def check(msg):
            return msg.author == interaction.user and msg.channel == interaction.channel
        
        items = []
        while True:
            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == '완료!':
                    if not items:
                        await interaction.followup.send("항목이 입력되지 않았습니다.")
                        return
                    break
                items.append(msg.content.strip())
            except asyncio.TimeoutError:
                await interaction.followup.send("제한 시간을 초과하여 종료합니다.")
                break
            
        if items:
            result = random.choice(items)

        result_message = "목록\n" + "\n".join(f"- {item}" for item in items)
            
        embed = discord.Embed(
            title="당첨!",
            description=f"{result}\n\n{result_message}",
            color=0x8FCE00
        )
        await interaction.followup.send(embed=embed)

    
    # type: 2
    async def gacha_voice_channel(self, interaction: discord.Interaction) -> None:
        # 음성 채널에 들어가 있는지 확인
        if not interaction.user.voice or not interaction.user.voice.channel:
            await interaction.response.send_message("음성 채널에 들어가 있어야 합니다. 음성 채널에 들어가신 후 다시 시도해주세요.")
            return
        
        voice_channel = interaction.user.voice.channel
        members = [member for member in voice_channel.members if not member.bot]

        member_mentions = " ".join(member.mention for member in members)

        member_items = {}

        await interaction.response.send_message(
            f"{member_mentions}\n각각 하나씩 항목을 작성해 주세요. 제한 시간은 60초 입니다.\n"
            "모든 멤버의 입력이 끝나면 자동으로 종료됩니다. 혹은 '완료!'를 입력하면 조기 종료가 가능합니다."
        )

        while True:
            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=lambda m: m.channel == interaction.channel and m.author in members)
                author = msg.author
                content = msg.content

                if content.lower() == '완료!':
                    break

                if author not in member_items:
                    member_items[author] = []

                if len(member_items[author]) == 0:
                    member_items[author].append(content.strip())

                if len(member_items) == len(members) and all(len(items) > 0 for items in member_items.values()):
                    break
            except asyncio.TimeoutError:
                await interaction.followup.send("제한 시간이 초과되어 종료합니다.")
                break

        if not member_items:
            await interaction.followup.send("아무도 항목을 입력하지 않았습니다.")
            return
        
        result_message = "목록\n"
        all_items = []
        for member, items in member_items.items():
            result_message += f"{member.display_name}: {', '.join(items)}\n"
            all_items.extend(items)

        if not all_items:
            await interaction.followup.send("입력된 항목이 없습니다.")
            return

        result = random.choice(all_items)
        embed = discord.Embed(
            title="당첨!",
            description=f"{result}\n\n{result_message}",
            color=0x8FCE00
        )
        await interaction.followup.send(embed=embed)


    # type: 3
    async def gacha_multiple(self, interaction: discord.Interaction) -> None:
        keyword = "!"
        await interaction.response.send_message(
            f"항목을 작성할 때 '{keyword}'로 시작해 주세요. ex) {keyword}딸기\n"
            "각 한사람당 하나씩만 작성 가능하며 제한 시간은 60초 입니다. 입력 완료 후 '완료!'라고 입력해 주세요."
        )

        member_items = {}
        while True:
            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=lambda m: m.channel == interaction.channel and (m.content.startswith(keyword) or m.content.lower() == '완료!'))
                author = msg.author
                content = msg.content

                if content.lower() == '완료!':
                    break

                if author not in member_items:
                    member_items[author] = []

                if len(member_items[author]) == 0: 
                    member_items[author].append(content[len(keyword):].strip())
                else:
                    await msg.reply("이미 항목을 입력하셨습니다. 추가로 입력할 수 없습니다.", mention_author=True) 
                    
            except asyncio.TimeoutError:
                await interaction.followup.send("제한 시간이 초과되어 종료합니다.")
                break

        if not member_items:
            await interaction.followup.send("아무도 항목을 입력하지 않았습니다.")
            return

        result_message = "목록\n"
        all_items = []
        for member, items in member_items.items():
            result_message += f"{member.display_name}: {', '.join(items)}\n"
            all_items.extend(items)

        if not all_items:
            await interaction.followup.send("입력된 항목이 없습니다.")
            return

        result = random.choice(all_items)
        embed = discord.Embed(
            title="당첨!",
            description=f"{result}\n\n{result_message}",
            color=0x8FCE00
        )
        await interaction.followup.send(embed=embed)
        

# Cog를 추가
async def setup(bot: commands.Bot) -> None: 
    await bot.add_cog(Gacha(bot))
