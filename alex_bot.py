import discord
from discord.ext import commands
import os
from os import getenv
import asyncio
import ctx
import time
import random
import site

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if ('boss') in message.content:
     #   msg = 'What do you want?'.format(message)
     #   await client.send_message(message.channel, msg)

    #if ('My boss') in message.content:
     #   msg = 'What do you want?'.format(message)
     #   await client.send_message(message.channel, msg)

    if message.content.startswith('?myname'):
        msg = 'I don\'t care your name {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        sleep(1)
        msg = 'Ok...Your name is: {0.author.display_name}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('?datetime'):
        msg = 'Your current date and time: ' + str(datetime.datetime.now())
        await client.send_message(message.channel, msg)
        msg = 'I have another time because I am in holidays, haha {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('?whoru'):
        msg = 'Did not introduced myself yet? My apologies, I\'m Your boss, the official Fortnite\'s CAD\'s player created by my own boss. Nice to meet you {0.author.mention}! You can see the list of commands that you can use by typing ?help'.format(message)
        await client.send_message(message.channel, msg)

  #  Leave ?help always the last one. Please update in GitHub any changes.
    if message.content.startswith('?help'):
        msg = 'Hi there! Here are the commands you can use with me so far: https://github.com/cibathleticsdev/archie-bot/blob/chorras/README.md#commands. My prefix is "?"'.format(message)
        await client.send_message(message.channel, msg)

  # message.content

    if ('hello boss') in message.content:
        msg = 'Hello {0.author.mention}, my padawan'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'How are you today {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

    if ('pepe') in message.content:
        a = 'El que te la mete hasta por el retrete!'
        b = 'El que te mete el nepe!'
        c = 'El que te la saca y te la mete!'
        d = 'El que hasta los huevos me mete'
        msg = 'Pepe, '.format(message) + random.choice([a, b, c, d])
        await client.send_message(message.channel, msg)

    if ('arturo') in message.content:
        a = 'El del ciruelo duro'
        b = 'El de mi polla con cianuro'
        msg = 'Arturo, '.format(message) + random.choice([a, b])
        await client.send_message(message.channel, msg)

    if ('fernando') in message.content:
        msg = 'El de los huevos colgando y la picha arrastrando!'.format(message)
        await client.send_message(message.channel, msg)

    if ('enrique') in message.content:
        msg = 'El que te la mete detrás del tabique!'.format(message)
        await client.send_message(message.channel, msg)

    if ('yolanda') in message.content:
        msg = 'La que folla mas que anda!'.format(message)
        await client.send_message(message.channel, msg)

    if ('not fine boss') in message.content:
        msg = 'well, hope you\'ll be ok {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if ('fine thanks boss') in message.content:
        msg = 'Cool, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'I\'m fine too :laughing:'.format(message)
        await client.send_message(message.channel, msg)

    if ('good night boss') in message.content:
        msg = 'Good night {0.author.mention}, see you towmorrow'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'stop watching youtube videos :laughing:'.format(message)
        await client.send_message(message.channel, msg)

    if ('hola') in message.content:
        msg = 'Pa\' ti mi cola {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = '{0.author.mention} y tu nariz conta mis bolas'.format(message)
        await client.send_message(message.channel, msg


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id='445639247647473676'), 'YourBoss is now online!')
    await client.change_presence(game=discord.Game(name="Fortnite"))


if __name__ == '__main__':
    import config
    client.run(config.token)
