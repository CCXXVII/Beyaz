#Discord bot
import discord
import os
import csv
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
client = commands.Bot(intents=intents, command_prefix='/', help_command=None)


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

    if message_content.startswith('<'):
        input_ids = tokenizer.encode(message.content, return_tensors='pt')
        attention_mask = input_ids.ne(0).type(torch.long)
        position_ids = torch.arange(input_ids.size()[1], dtype=torch.long, device=input_ids.device)
        position_ids = position_ids.unsqueeze(0).expand_as(input_ids)
        output = model.generate(input_ids,attention_mask=attention_mask)
        tokenizer.decode(output[0])
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        await message.channel.send(generated_text)

@client.command()
async def category(ctx, category: str):
    questions = []
    with open('sorular.csv', 'r', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == category:
                questions.append(row[1:])

    if not questions:
        await ctx.send(f'{category} is not a valid category')
        return

    question = random.choice(questions)
    await ctx.send(question[0])
    await ctx.send('Answers:' + ', '.join(question[2]))
    await answer(ctx, question)

@client.command()
async def answer(ctx, question):
    if question[1] == answer:
        await ctx.send('Correct!')
    else:
        await ctx.send('Incorrect!, the correct answer is ' + question[1])














































# Running with the token
f = open('key.json',)
with open('key.json') as f:
    data = json.load(f)
    token = data['token']
    print(token)
    
client.run(token)




