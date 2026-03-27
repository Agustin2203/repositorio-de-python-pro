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
async def bot1(ctx):
    await ctx.send("¡Hola! ¡Esta versión de mi te ayudará con el tema de residuos y ecologia!☘️🌱")
@bot.command()
async def ecologia(ctx):
    await ctx.send("Para ayudar a la ecologia puedes: reciclar, plantar plantas, flores o arboles y no crear humo.")
@bot.command()
async def consejo(ctx):
    a = random.randint(1, 5)
    if a == 1:
        await ctx.send("¡Si ves algún residuo tirado por la calle, tiralo Tú a su contenedor correspondiente.")
    elif a == 2:
        await ctx.send("¡Planta alguna flor, arbol o planta de verdura!")
    elif a == 3:
        await ctx.send("¡Siempre recicla!")
    elif a == 4:
        await ctx.send("¡Tira tus residuos en sus correspondientes contenedores!")
    elif a == 5:
        await ctx.send("¡No hagas grandes fogatas, producen mucho humo!")
@bot.command()
async def residuos(ctx):
    await ctx.send("Clasificacion de residuos: Reciclables, organicos, no reciclables.")
    await ctx.send("Reciclables: papel, carton, plásticos, vidrio y metales (Todos estos estando secos y limpios).")
    await ctx.send("Organicos: cascara de fruta, restos de verdura, yerba, sacos de té, cascara de huevo y restos de comidas naturales")
    await ctx.send("No reciclables: papel sucio o mojado, cualquier tipo de descartable, colas de cigarro, polvo del piso y en general cosas que no estan en las otras 2 categorías.")
bot.run("token")
