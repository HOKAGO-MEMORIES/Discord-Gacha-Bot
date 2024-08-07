import discord
import random
import asyncio

from discord import app_commands
from discord.ext import commands
from typing import Literal


class Team(commands.Cog, name="team"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.active_commands = {}


    @app_commands.command(
        name="팀짜기",
        description="무작위로 팀을 짜봅시다."
    )
    @app_commands.describe(
        type="1: 현재 음성채널에 함께 있는 모든 사람과 팀을 짭니다.  /  2: 원하는 사람을 선택 후 팀을 짭니다.",
        team_num="팀의 수를 정합니다.",
    )
    async def team(self, interaction: discord.Interaction, type: Literal[1, 2], team_num: int) -> None:
        if interaction.user.id in self.active_commands:
            await interaction.response.send_message("이미 명령어를 실행 중입니다. 실행 중인 명령어가 완료된 후 다시 시도해 주세요.")
            return
        
        if team_num < 2:
            await interaction.response.send_message("팀 수는 2개 이상이어야 합니다.")
            return
        
        self.active_commands[interaction.user.id] = True

        try:
            if type == 1:
                await self.team_voice_channel(interaction, team_num)
            elif type == 2:
                await self.team_multiple(interaction, team_num)
        finally:
            del self.active_commands[interaction.user.id]

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
            "제한 시간은 60초입니다."
        )

        try:
            msg = await self.bot.wait_for('message', timeout=60.0, check=check)
            members = [m for m in msg.mentions if not m.bot]

            if len(members) < team_num:
                await interaction.followup.send("팀 수보다 참가할 멤버 수가 적습니다.")
                return
        except asyncio.TimeoutError:
            await interaction.followup.send("제한 시간이 초과되어 종료합니다.")
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
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Team(bot))
