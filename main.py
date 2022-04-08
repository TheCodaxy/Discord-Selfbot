#<---------------------------->
from turtle import clear
import discord
from colorama import Fore, Style
from discord.ext import commands
from settings import token
from settings import prefix
from settings import chname
from settings import flood_msg
#<---------------------------->

#<---------------------------->
fVermelho = "\033[1;31m"
tVerdeClaro  = "\033[1;92m"
tReset = "\033[0;0m"
#<---------------------------->

#<---------------------------->
bot = commands.Bot(command_prefix = prefix, self_bot = True)

@bot.event
async def on_ready():
	print(tVerdeClaro + 'λ ► Selfbot ativado!')
#<---------------------------->

#<---------------------------->
@bot.command()
async def raid(ctx):
  guild = ctx.guild
  while True:
    await guild.create_text_channel(name=chname)

@bot.command()
async def raid2(ctx):
  guild = ctx.guild
  while True:
    await guild.create_voice_channel(name=chname)

@bot.command()
async def flood(ctx):
  while True:
    await ctx.send(flood_msg)

@bot.command()
async def purge(message):
  async for msg in message.channel.history(limit=10000):
    if msg.author == bot.user:
      try:
        await msg.delete()
      except:
        pass

@bot.command()
async def avatar(ctx):
  await ctx.send(ctx.author.avatar_url)

@bot.command()
async def sobre(ctx):
  await ctx.send('```SelfBot - By Codaxy 水\n-------------------\n» Versão - 1.2\n» Linguagem - Python\n» Api - Discord.py\n» Agradecimentos - Blackx``` https://www.youtube.com/channel/UCgc5IlYHfFIv2QNN8BSdxDQ')

@bot.command()
async def ajuda(ctx):
  await ctx.send('```SelfBot - By Codaxy 水\n-------------------\nComandos:\n» {}ajuda - Exibe os comandos disponíveis.\n» {}sobre - Informações sobre o selfbot\n» {}raid - Cria diversos canais de texto.\n» {}raid2 - Cria diversos canais de voz.\n» {}purge - Deleta todas as suas mensagens.\n» {}avatar - Mostra seu avatar atual.\n» {}flood - Flooda mensagens no chat.```' .format(prefix, prefix, prefix, prefix, prefix, prefix, prefix))
#<---------------------------->

#<---------------------------->
while True:
  try:
    bot.run(token, bot=False)
  except:
    clear()
    print(fVermelho + 'λ ► O token é inválido')
    print(tReset + '')
    quit()
#<---------------------------->
