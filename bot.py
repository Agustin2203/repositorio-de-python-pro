import discord
import bot2_logic
bl = bot2_logic
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("Hola!")
    elif message.content.startswith('$bye'):
        await message.channel.send("👋")
    elif message.content.startswith('$password'):
        await message.channel.send(bl.gen_pass(10))
    elif message.content.startswith("$tirar moneda"):
        await message.channel.send(bl.tirar_moneda())
    elif message.content.startswith("$d"):
        await message.channel.send("$")
    else:
        None
