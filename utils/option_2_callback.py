# option_2 버튼에 대한 콜백함수 정의
# 유저 중에서 당첨자 추첨
from discord.ext import ui

async def on_option_2_click(interaction):

    await interaction.response.send_message()
