import asyncio
import discord
import os
import time


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("hello world, lmao")

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith("Your server has been booped. Remember to do this again in 2 hours! Check out other servers or add yours here: https://www.unfocused.org/"):
    await message.channel.send("i will remind you again in 2 hrs. see ya then!")
    await asyncio.sleep(60*60*2)
    await message.channel.send("where are you? bet you forgot to boop again.... BOOP NOW!!!")


client.run('MTI4NTIyNzQ5NDA5MzYyMzMzOQ.GfvYCv.lr6q_X51TEhhVrUFZH5O9-80bdEbu_POICLCDQ')


