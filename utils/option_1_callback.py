# option_1 버튼에 대한 콜백함수 정의
# 여러 키워드 입력 후 하나 추첨
from discord.ext import ui

async def on_option_1_click(interaction):

    await interaction.response.send_message()
