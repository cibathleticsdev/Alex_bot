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

    #if ('boss') in message.content:
     #   msg = 'What do you want?'.format(message)
     #   await client.send_message(message.channel, msg)

    #if ('MyBoss') in message.content:
     #   msg = 'What do you want?'.format(message)
     #   await client.send_message(message.channel, msg)

    if message.content.startswith('?myname'):
        msg = 'I don\'t care your name {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        sleep(1)
        msg = 'Ok\.\.\.Your name is: {0.author.display_name}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('?datetime'):
        msg = 'Your current date and time: ' + str(datetime.datetime.now())
        await client.send_message(message.channel, msg)
        msg = 'I have another time because I am in holidays, haha {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

  # do not remove '?update' !!
    if message.content.startswith('?update'):
        msg = 'Wait a few seconds...'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Updating Your boss'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Your boss is now offline!'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Party is on!:smile::grinning::smiley::tada: '.format(message)
        await client.send_message(message.channel, msg)
        os.system("python3 ~/discord/update.py")
        time.sleep(5)
        exit()

  #  if message.content.startswith('?add'):
  #      async def add(ctx, a: int, b: int):
  #      await client.send(a+b)

  #  Leave !help always the last one. Please update in GitHub any changes.
    if message.content.startswith('?help'):
        msg = 'Hi there! Here are the commands you can use with me so far: https://github.com/cibathleticsdev/archie-bot/blob/chorras/README.md#commands. My prefix is "?"'.format(message)
        await client.send_message(message.channel, msg)


    #message.content

    if ('pepe') in message.content:
        a = 'El que te la mete hasta por el retrete!'
        b = 'El que te mete el nepe!'
        c = 'El que te la saca y te la mete!'
        d = 'El que hasta los huevos me mete'
        msg = 'Pepe, '.format(message) + random.choice([a, b, c, d])
        await client.send_message(message.channel, msg)

    if ('hello boss') in message.content:
        msg = 'Hello {0.author.mention}, my little padawan'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'How are you today {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)


    if ('good night boss') in message.content:
        msg = 'Good night {0.author.mention}, see you towmorrow'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'stop watching youtube videos :laughing:'.format(message)
        await client.send_message(message.channel, msg)

    if ('fine thanks boss') in message.content:
        msg = 'Cool, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'I\'m fine too :laughing:'.format(message)
        await client.send_message(message.channel, msg)

    if ('not fine boss') in message.content:
        msg = 'well, hope you\'ll be ok {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if ('hola') in message.content:
        msg = 'Pa\' ti mi cola {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = '{0.author.mention} y tu nariz conta mis bolas'.format(message)
        await client.send_message(message.channel, msg

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
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id='481951758722138113'), 'YourBoss is now online!')
    await client.change_presence(game=discord.Game(name="CADevelopers | ?help"))

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
