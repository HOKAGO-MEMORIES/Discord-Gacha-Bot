import discord
from discord import app_commands
import random
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bot import client

@client.tree.command(name='마법의소라고동님')
async def MagicConch(interaction: discord.Interaction):
    responses = [
        "Yes.", "No.", "Maybe.", "Ask again later.", "Definitely.", 
        "I don't think so.", "Without a doubt.", "Absolutely not.", 
        "Sure.", "I can't tell.", "Absolutely.", "Very doubtful."
    ]
    response = random.choice(responses)
        
    # 로컬 이미지 파일 경로
    image_path = os.path.join('images', 'magic_conch.png')
    file = discord.File(image_path, filename='magic_conch.png')

    embed = discord.Embed(title="Magic Conch", description=response, color=0x00ff00)
    embed.set_image(url="attachment://magic_conch.png")  # 파일명을 참조합니다

    await interaction.response.send_message(embed=embed, file=file)
   
# Cog를 추가
async def setup(bot):
    await bot.add_cog(MagicConch(bot))
    bot.tree.add_command(MagicConch(bot).magic_conch)
