#Discord bot
import discord
import os
import random
import dotenv
from dotenv import load_dotenv
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, command_prefix='!', help_command=None)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == 'Karantina Geceleri':
            break
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_content = message.content.lower()

    if message_content.startswith('!beyaz'):
        await message.channel.send('Hey! I am Beyaz, the official bot of Karantina Geceleri Server. I am still in development, but I will be able to do a lot of things soon. Stay tuned!')



# Run the bot but dont show the token
token = os.getenv('token')
client.run(token)




