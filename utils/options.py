# 각 버튼에 대한 정의
from discord.ext import ui
from option_1_callback import on_option_1_click
from option_2_callback import on_option_2_click
from option_3_callback import on_option_3_click

# 여러 키워드 입력 후 하나 추첨
option_1 = ui.Button(label='1번', custom_id='draw_button_1')
option_1.callback(on_option_1_click)

# 유저 중에서 당첨자 추첨
option_2 = ui.Button(label='2번', custom_id='draw_button_2')
option_2.callback(on_option_2_click)

# 마법의 소라고동
option_3 = ui.Button(label='3번', custom_id='draw_button_3')
option_3.callback(on_option_3_click)