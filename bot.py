# bot.py
import os
import discord, random
from discord import channel
from discord import user
from discord.ext.commands.core import group
from discord.flags import Intents
from dotenv import load_dotenv
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
TOKEN = 'OTEyMDU1Nzg2Njk4NjAwNTEw.YZqYJA.-dmXGUlqMDtXflWnHw8p5Jln5yc'
bot = commands.Bot(command_prefix='.')
client = discord.Client()




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    

# @client.event
# async def on_member_join(member):
#     gluid = client.get_guild(912057316705189931)
#     channel = client.get_channel(912057316705189931)
#     await gluid.send(f'Welcome to the server {member.mention}')
#     await member.send(f'Welcome to the {channel.name} server, {member.mention}')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}')
        elif user_message.lower() == '!random':
            response = f'this is your random number {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send(f'Anywhere')
        return

# sends message every 1 mins
@tasks.loop(minutes=1)
async def my_background_task():
    channel = client.get_channel(912057316705189931)
    await channel.send('TEST!')
    
@my_background_task.before_loop
async def my_background_task_before_loop():
    await client.wait_until_ready()

my_background_task.start()
client.run(TOKEN)
