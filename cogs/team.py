import discord
import random
import asyncio

from discord import app_commands
from discord.ext import commands
from typing import Literal


class Team(commands.Cog, name="team"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="팀짜기",
        description="무작위로 팀을 짜봅시다."
    )
    @app_commands.describe(
        type="1: 현재 음성채널에 함께 있는 모든 사람과 팀을 짭니다. 2: 원하는 사람을 선택 후 팀을 짭니다.",
        team_num="팀의 수를 정합니다."
    )
    async def team(self, interaction: discord.Interaction, type: Literal[1, 2], team_num: int):
        if team_num < 2:
            await interaction.response.send_message("팀 수는 2개 이상이어야 합니다.")
            return
        
        if type == 1:
            await self.team_voice_channel(interaction, team_num)
        elif type == 2:
            await self.team_multiple(interaction, team_num)


    # type: 1
    async def team_voice_channel(self, interaction: discord.Interaction, team_num: int) -> None:
        # 음성 채널에 들어가 있는지 확인
        if not interaction.user.voice or not interaction.user.voice.channel:
            await interaction.response.send_message("음성 채널에 들어가 있어야 합니다. 음성 채널에 들어가신 후 다시 시도해주세요.")
            return

        voice_channel = interaction.user.voice.channel
        members = [member for member in voice_channel.members if not member.bot]

        if len(members) < team_num:
            await interaction.response.send_message("팀 수보다 음성 채널에 있는 사람이 적습니다.")
            return
        
        random.shuffle(members)
        teams = [[] for _ in range(team_num)]

        for index, member in enumerate(members):
            teams[index % team_num].append(member)

        result_message = ""
        for i, team in enumerate(teams):
            result_message += f"**팀 {i+1}**\n" + "\n".join(member.display_name for member in team) + "\n\n"

        embed = discord.Embed(
            title="팀 결과",
            description=result_message,
            color=0x2986CC
        )

        await interaction.response.send_message(embed=embed)



    # type: 2
    async def team_multiple(self, interaction: discord.Interaction, team_num: int) -> None:
        def check(msg):
            return msg.author == interaction.user and msg.channel == interaction.channel

        await interaction.response.send_message(
            "팀에 참가할 멤버를 멘션으로 선택하세요. 예시: @user1 @user2 @user3 ...\n"
            "모두 선택한 후 '완료!'라고 입력하세요. 제한 시간은 60초입니다."
        )

        members = []
        try:
            while True:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                if msg.content.lower() == '완료!':
                    if not members:
                        await interaction.followup.send("선택된 멤버가 없습니다.")
                        return
                    break
                else:
                    new_members = [m for m in msg.mentions if not m.bot]
                    members.extend(new_members)
                    if len(members) >= team_num:
                        break
        except asyncio.TimeoutError:
            await interaction.followup.send("제한 시간을 초과하여 종료합니다.")
            return

        if len(members) < team_num:
            await interaction.followup.send("팀 수보다 참가할 멤버 수가 적습니다.")
            return

        random.shuffle(members)
        teams = [[] for _ in range(team_num)]

        for index, member in enumerate(members):
            teams[index % team_num].append(member)

        result_message = ""
        for i, team in enumerate(teams):
            result_message += f"**팀 {i+1}**\n" + "\n".join(member.display_name for member in team) + "\n\n"

        embed = discord.Embed(
            title="팀 결과",
            description=result_message,
            color=0x2986CC
        )
        await interaction.followup.send(embed=embed)



# Cog를 추가
async def setup(bot) -> None:
    await bot.add_cog(Team(bot))
