# option_2 버튼에 대한 콜백함수 정의 (2번 버튼 눌렀을 때 발동되는 이벤트)
from discord.ext import ui

async def on_option_2_click(interaction):

    await interaction.response.send_message()
