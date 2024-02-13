# option_3 버튼에 대한 콜백함수 정의 (3번 버튼 눌렀을 때 발동되는 이벤트)
from discord.ext import ui

async def on_option_3_click(interaction):

    await interaction.response.send_message()
