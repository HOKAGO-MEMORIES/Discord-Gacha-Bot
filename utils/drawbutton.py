# 각각 버튼에 대한 로직
from discord import ui
from utils import option_1_callback, option_2_callback, option_3_callback

class DrawButton(ui.Button):
    def __init__(self, ctx, view, label, custom_id, callback=None, **kwargs):
        super().__init__(label, custom_id=custom_id, **kwargs)
        self.ctx = ctx
        self.view = view
        self.callback_func = callback

    async def callback(self, interaction):
        if self.custom_id == 'draw_button_1':
            await option_1_callback.on_option_1_click(self.ctx, interaction)
        elif self.custom_id == 'draw_button_2':
            await option_2_callback.on_option_1_click(self.ctx, interaction)
        elif self.custom_id == 'draw_button_3':
            await option_3_callback.on_option_1_click(self.ctx, interaction)
        else:
            if self.callback_func:
                await self.callback_func(interaction)
