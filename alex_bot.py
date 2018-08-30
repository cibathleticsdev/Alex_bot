import discord
from discord.ext import commands
import os
from os import getenv
import asyncio
import ctx
import time
import datetime
import random
import site
import sys
# hide config.py
sys.path.insert(0, '/home/dietpi/discord')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if ('pepe') in message.content:
        a = 'El que te la mete hasta por el retrete!'
        b = 'El que te mete el nepe!'
        c = 'El que te la saca y te la mete!'
        d = 'El que hasta los huevos me mete'
        msg = 'Pepe, '.format(message) + random.choice([a, b, c, d])
        await client.send_message(message.channel, msg)

    if ('enrique') in message.content:
        msg = 'El que te la mete detrás del tabique!'.format(message)
        await client.send_message(message.channel, msg)

    if ('yolanda') in message.content:
        msg = 'La que folla mas que anda!'.format(message)
        await client.send_message(message.channel, msg)

    if ('fernando') in message.content:
        msg = 'El de los huevos colgando y la picha arrastrando!'.format(message)
        await client.send_message(message.channel, msg)

    if ('arturo') in message.content:
        a = 'El del ciruelo duro'
        b = 'El de mi polla con cianuro'
        msg = random.choice([a, b]).format(message)
        await client.send_message(message.channel, msg)

@client.event
async def multiply(ctx, a: int, b: int):
    if message.content.startswith('!multiply'):
        print('hello')
	#await ctx.send(a*b)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id='481951758722138113'), 'Archie is now online!')
    await client.change_presence(game=discord.Game(name="CAD Developers | !help"))

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#while True:
 #  input_state = GPIO.input(18)
  # if input_state == False:
    #msg = 'Archie is now rebooting'.format(message)
    #await client.send_message(message.channel, msg)
    #msg = 'Status: disconected'.format(message)
    #await client.send_message(message.channel, msg)
   # time.sleep(1)
   # os.system("sudo reboot")
   # time.sleep(0.2)

if __name__ == '__main__':
    import config
    client.run(config.token)
