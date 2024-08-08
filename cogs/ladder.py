import discord
import random
import asyncio

from discord import app_commands
from discord.ext import commands
from typing import Literal


class Ladder(commands.Cog, name="ladder"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.active_commands = {}


    @app_commands.command(
        name="사다리",
        description="정하기 어렵다면 사다리를 타봅시다."
    )
    @app_commands.describe(
        type="1: 현재 음성채널에 함께 있는 모든 사람과 팀을 짭니다.  /  2: 원하는 사람을 선택 후 팀을 짭니다.",
        input_type="1: 혼자 항목을 작성합니다.  /  2: 참여하는 모든 사람과 항목을 작성합니다.",
    )
    async def team(self, interaction: discord.Interaction, type: Literal[1, 2], input_type: Literal[1, 2]) -> None:
        if interaction.user.id in self.active_commands:
            await interaction.response.send_message("이미 명령어를 실행 중입니다. 실행 중인 명령어가 완료된 후 다시 시도해 주세요.")
            return
        
        self.active_commands[interaction.user.id] = True

        try:
            if type == 1:
                await self.ladder_voice_channel(interaction, input_type)
            elif type == 2:
                await self.ladder_multiple(interaction, input_type)
        finally:
            del self.active_commands[interaction.user.id]


    # type: 1
    async def ladder_voice_channel(self, interaction: discord.Interaction, input_type: int) -> None:
        # 음성 채널에 들어가 있는지 확인
        if not interaction.user.voice or not interaction.user.voice.channel:
            await interaction.response.send_message("음성 채널에 들어가 있어야 합니다. 음성 채널에 들어가신 후 다시 시도해주세요.")
            return

        voice_channel = interaction.user.voice.channel
        members = [member for member in voice_channel.members if not member.bot]

        if input_type == 1:
            await self.get_items_single(interaction, members)
        else:
            await self.get_items_multiple(interaction, members)



    # type: 2
    async def ladder_multiple(self, interaction: discord.Interaction, input_type: int) -> None:
        def check(msg):
            return msg.author == interaction.user and msg.channel == interaction.channel

        await interaction.response.send_message(
            "사다리타기에 참가할 멤버를 멘션으로 선택하세요. 예시: @user1 @user2 @user3 ...\n"
            "제한 시간은 60초입니다."
        )

        try:
            msg = await self.bot.wait_for('message', timeout=60.0, check=check)
            members = [m for m in msg.mentions if not m.bot]

            if not members:
                await interaction.followup.send("유효한 멤버가 선택되지 않았습니다. 명령어를 다시 실행해주세요.")
                return
        except asyncio.TimeoutError:
            await interaction.followup.send("제한 시간이 초과되어 종료합니다.")
            return
        
        if input_type == 1:
            await self.get_items_single(interaction, members)
        else:
            await self.get_items_multiple(interaction, members)



    async def get_items_single(self, interaction: discord.Interaction, members: list) -> None:
        await interaction.followup.send(
            "항목을 별도의 메시지로 작성해 주세요. ex) 바나나, 사과, 오렌지를 각각의 메시지로 입력합니다. \n"
            "제한 시간은 60초입니다. 인원수에 맞춰서 작성하면 자동으로 종료됩니다."
        )

        def check(msg):
            return msg.author == interaction.user and msg.channel == interaction.channel
        
        items = []
        while len(items) < len(members):
            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                items.append(msg.content.strip())
            except asyncio.TimeoutError:
                await interaction.followup.send("제한 시간이 초과되어 종료합니다.")
                return
            
        await self.generate_ladder_result(interaction, members, items)



    async def get_items_multiple(self, interaction: discord.Interaction, members: list) -> None:
        await interaction.followup.send(
            "각각 한명씩 하나의 항목을 작성해 주세요. 제한 시간은 60초입니다. \n"
            "모든 멤버의 입력이 끝나면 자동으로 종료됩니다."
        )

        members_items = {member: [] for member in members}
        while len([items for items in members_items.values() if len(items) > 0]) < len(members):
            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=lambda m: m.channel == interaction.channel and m.author in members)
                author = msg.author
                content = msg.content

                if len(members_items[author]) == 0:
                    members_items[author].append(content.strip())
                else:
                    await msg.reply("이미 항목을 입력하셨습니다. 추가로 입력할 수 없습니다.", mention_author=True)
            except asyncio.TimeoutError:
                await interaction.followup.send("제한 시간이 초과되어 종료합니다.")
                return
            
        items = [item[0] for item in members_items.values()]
        await self.generate_ladder_result(interaction, members, items)

    

    async def generate_ladder_result(self, interaction: discord.Interaction, members: list, items: list) -> None:
        random.shuffle(items)
        result_message = ""
        for member, item in zip(members, items):
            result_message += f"{member.display_name} -> {item}\n"

        embed = discord.Embed(
            title="사다리타기 결과",
            description=result_message,
            color=0xce7e00
        )
        await interaction.followup.send(embed=embed)

# Cog를 추가
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ladder(bot))
