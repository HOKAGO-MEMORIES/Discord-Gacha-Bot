# option_3 버튼에 대한 콜백함수 정의
# 마법의 소라고동
from discord.ext import ui

async def on_option_3_click(interaction):

    await interaction.response.send_message()
