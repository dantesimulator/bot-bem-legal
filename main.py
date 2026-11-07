from model import get_class
import discord
from discord.ext import commands
import os,requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print('seu Bot está pronto!')
@bot.command()
async def classificar(ctx):
    if not ctx.message.attachments:
        await ctx.send("Envie uma imagem.")
    else:
        imagem = ctx.message.attachments[0]
        caminho = imagem.filename
        await imagem.save(caminho)
        classe, confianca = get_class(caminho)
        if classe == "Desconhecido":
            await ctx.send(
                "Desculpe, não tenho certeza do que "
                "está sendo mostrado na imagem."
            )
        else:
            porcentagem = confianca * 100
            await ctx.send(
                f"Eu reconheci: **{classe}**\n"
                f"Confiança: **{porcentagem:.1f}%**"
            )
        os.remove(caminho)
bot.run('')
    