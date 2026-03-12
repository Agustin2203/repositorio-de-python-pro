import discord
import bot2_4
from discord.ext import commands
bl = bot2_4
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send("hi")
@bot.command()
async def bye(ctx):
    await ctx.send("👋")
@bot.command()
async def password(ctx):
    await ctx.send(bl.gen_pass(10))
@bot.command()
async def tirarmoneda(ctx):
    await ctx.send(bl.tirar_moneda())
@bot.command()
async def he(ctx):
    await ctx.send("he")
