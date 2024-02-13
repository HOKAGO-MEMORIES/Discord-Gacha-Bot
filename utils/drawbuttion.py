# 각각 버튼에 대한 로직
from discord.ext import ui
from options import *

class DrawButton(ui.Button):
    def __init__(self, ctx, view, label, custom_id, callback=None, **kwargs):
        super().__init__(label, custom_id=custom_id, **kwargs)
        self.ctx = ctx
        self.view = view
        self.callback_func = callback

    async def callback(self, interaction):
        if self.custom_id == 'draw_button_1':
            await on_option_1_click(interaction)
        elif self.custom_id == 'draw_button_2':
            await on_option_2_click(interaction)
        elif self.custom_id == 'draw_button_3':
            await on_option_3_click(interaction)
        else:
            if self.callback_func:
                await self.callback_func(interaction)
