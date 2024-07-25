import random
import discord
import os

from discord.ext import commands
from discord.ext.commands import Context

class MagicConch(commands.Cog, name="magicconch"):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.hybrid_command(
        name="마법의소라고동님",
        description="소라... 고동이라고? 이거 말이니?"
    )
    async def MagicConch(self, context: Context, *, question: str) -> None:
        answers = [
            "확실해.",
            "주변에다 물어봐.",
            "의심의 여지가 없어.",
            "분명히 그래.",
            "내가 보기엔 그래.",
            "아마도 그래.",
            "전망이 좋아.",
            "응.",
            "예감이 좋아.",
            "포기하지 마.",
            "나중에 다시 물어봐.",
            "지금은 안돼.",
            "조금 더 기다려.",
            "호흡을 가다듬고 다시 물어봐.",
            "기대하지 마.",
            "내 대답은 '아니'야.",
            "확률이 매우 높아.",
            "부정적 확률이 매우 높아.",
            "그다지 좋지 않아.",
            "전망이 좋지 않아.",
            "매우 의심스러워.",
            "상당히 그래.",
            "오늘은 그런 날이야.",
            "지금은 확실하지 않아.",
            "너의 직감을 믿어.",
            "다시 한 번 물어봐.",
            "곧 알게 될거야.",
            "절대 안돼.",
            "현재는 아니야.",
            "질문을 다시 생각해.",
            "아니.",
            "조금 더 기다려.",
            "자신감을 가져.",
            "오늘은 안 돼.",
            "곧 알게 될거야.",
            "의심해.",
            "그러지마.",
            "참고 기다려.",
            "글쎄.",
            "망설이지 마.",
            "걱정하지 마.",
            "좀 더 고민해봐.",
            "쓸데없는 질문.",
            "다시 생각해.",
            "할 수 있다면 해.",
            "언젠가.",
            "한번 시도해.",
            "그럴리 없어.",
            "한 숨 돌리고 다시 생각해.",
            "가능해.",
            "괜찮아 보여.",
            "꿈도 꾸지마.",
            "내 정보로는 별로.",
            "너 마음대로 해.",
            "생각하는 대로 돼.",
            "너는 이미 답을 알고 있어.",
            "어차피 마음대로 할거면서.",
        ]


        embed = discord.Embed(
            title="소라고동님의 답변...", 
            description=f"{random.choice(answers)}", 
            color=0x9900FF
        )

        embed.set_footer(text=f"너의 질문 : {question}")
    
        # 로컬 이미지 첨부
        current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(current_directory, 'resources', 'magic_conch.png')
        file = discord.File(image_path, filename='magic_conch.png')
        embed.set_image(url="attachment://magic_conch.png")

        await context.send(file=file, embed=embed)

   
async def setup(bot) -> None:
    await bot.add_cog(MagicConch(bot))
