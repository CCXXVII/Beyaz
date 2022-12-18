#Discord bot
import discord
import os
import random
import dotenv
import json
from dotenv import load_dotenv
from discord.ext import commands
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot_small-90M")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot_small-90M")


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

    if message_content.startswith('<'):
        input_ids = tokenizer.encode(message.content, return_tensors='pt')
        attention_mask = input_ids.ne(0).type(torch.long)
        position_ids = torch.arange(input_ids.size()[1], dtype=torch.long, device=input_ids.device)
        position_ids = position_ids.unsqueeze(0).expand_as(input_ids)
        output = model.generate(input_ids,attention_mask=attention_mask)
        tokenizer.decode(output[0])
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        await message.channel.send(generated_text)


    if message_content.startswith('!beyaz'):
        await message.channel.send('Hey! I am Beyaz, the official bot of Karantina Geceleri Server. I am still in development, but I will be able to do a lot of things soon. Stay tuned!')











































# Running with the token
f = open('config.json',)
with open('config.json') as f:
    data = json.load(f)
    token = data['token']
    print(token)
    
client.run(token)




