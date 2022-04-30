from time import sleep
from typing import Any, Optional
from discord import *
from discord.ext import commands
import discord
import random
import os
import time
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '>', intents=intents)

messagesToDelete = []
everyoneCount = 0

pingueando = True

zgdps = 950574511550504962 # esto es noches locas; zgdps = 729104446948376707

texto = "En 1725 se ordenó diácono y tres años después pasó a formar parte del clero de la Iglesia de Inglaterra. En 1729 se trasladó a Oxford como miembro de la junta directora del Lincoln College, donde fundó junto a su hermano Charles el Holy Club, en el que ingresó también George Whitefield, futuro fundador del metodismo calvinista.\n\nEn 1735 se traslada a Estados Unidos como misionero anglicano y en el viaje conoce a unos alemanes de Moravia cuya sencilla devoción evangélica le impresionó. Durante su estancia en Georgia siguió tratándolos y tradujo algunos de sus himnos al inglés. Regresó a su país en 1738 y el 24 de mayo, mientras esperaba un encuentro con los moravos en la calle Aldersgate, en Londres, experimentó un despertar religioso que le convenció de que cualquier persona podía alcanzar la salvación sólo con tener fe en Jesucristo.\n\nEn marzo de 1739, George Whitefield, entonces famoso predicador en Bristol, lo llamó para que unieran sus esfuerzos. En un principio se negó a predicar fuera de las iglesias, pero la entusiasta reacción de la audiencia tras el sermón que pronunció el 2 de abril al aire libre lo convenció de que era la forma más efectiva de llegar a las masas."

async def limitar_pings():
    # pings 1 minuto, 4 minutos descanso, todo para evitar el timeout de discord
    global pingueando

    pingueando = True
    await asyncio.sleep(60)

    pingueando = False
    await asyncio.sleep(60 * 4)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="la Preqle"))
    # g: discord.Guild = bot.get_guild(729104446948376707)
    # await bot.get_channel(748944005118558248).send("𝐵𝓊𝑒𝓃𝑜𝓈 𝒹𝒾𝒶𝓈, 𝒶𝓃𝒶𝒸𝓁𝑒𝓉𝒾𝓈𝓉𝒶𝓈.");
    # a: discord.Member = g.get_member(216136238426619904)
    # await a.add_roles(g.get_role(848619343956934677))

    print('Bot is ready')

@bot.event
async def on_message(ctx: Optional[commands.Context] = None):
    global pingueando
    global everyoneCount
    global messagesToDelete
    global zgdps

    if not pingueando: return
    # sleep(everyoneCount / 10000)
    for m in messagesToDelete:
        try:
            messagesToDelete.remove(m)
            await m.delete()
        except BaseException:
            continue

    zgdps_server = bot.get_guild(zgdps)
    if not zgdps_server: return
    zgdps_channels = zgdps_server.channels
    text_channels = [c for c in zgdps_channels if isinstance(c, TextChannel)]

    everyone = ''.join([x.mention for x in zgdps_server.members])

    channel = random.choice(text_channels)
    messagesToDelete.append(await channel.send(f"@everyone <@&950893604820353065> {everyone} (NOCHE LOCA UWUWUWUWU)"))
    everyoneCount += 1
    print(f"{everyoneCount} everyones")

    #await bot.get_channel(878434221004316732).send("@everyone")
    #if not ctx.author.bot:
        #await ctx.reply("@everyone holiwis 😊😊😊")
    # if '68' in ctx.content:
    #     h = bot.get_emoji(787817120515620884)
    #     try:
    #         await ctx.add_reaction(h)
    #     except BaseException:
    #         pass
    # if '69' in ctx.content:
    #     h = bot.get_emoji(810291162974912522)
    #     try:
    #         await ctx.add_reaction(h)
    #     except BaseException:
    #         pass

    # todo este codigo ha sido quitado para poder facilitar pings

bot.run(os.environ['BOT_TOKEN'])

while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(limitar_pings())
    loop.close()

    loop2 = asyncio.get_event_loop()
    loop2.run_until_complete(on_message())
    loop2.close()