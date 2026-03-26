import discord
import os
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def residuos(ctx):
    await ctx.send("Clasificacion de residuos: Resiclables, organicos, no resiclables.")
    await ctx.send("Resiclables: papel, carton, plásticos, vidrio y metales (Todos estos estando secos y limpios).")
    await ctx.send("Organicos: cascara de fruta, restos de verdura, yerba, sacos de té, cascara de huevo y restos de comidas naturales")
    await ctx.send("No resiclables: papel sucio o mojado, cualquier tipo de descartable, colas de cigarro, polvo del piso y en general cosas que no estan en las otras 2 categorías.")
bot.run("Token.txt")
