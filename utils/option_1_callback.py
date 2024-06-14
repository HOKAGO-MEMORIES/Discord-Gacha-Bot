# option_1 버튼에 대한 콜백함수 정의
# 여러 키워드 입력 후 하나 추첨
from discord.ext import commands
import random

async def on_option_1_click(interaction):
    
    await interaction.response.send_message("키워드를 엔터로 구분해서 입력해주세요. 입력이 끝났다면 '완료'를 입력해주세요. \n제한 시간은 1분입니다.")
    
    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel
    
    try:
        keywords = []
        while True:
            keyword_input = await interaction.bot.wait_for('message', check=check, timeout=60.0)
            if keyword_input.content.lower() == "완료":
                break
            else:
                keywords.append(keyword_input.content)
                
        if not keywords:
            await interaction.response.send_message("입력된 키워드가 없습니다.")
        else:
            selected_keyword = random.choice(keywords)
            await interaction.response.send_message(f'선택된 키워드는 : {selected_keyword} 입니다!')
          
    except TimeoutError:
        await interaction.response.send_message("제한 시간이 지났습니다.")
        