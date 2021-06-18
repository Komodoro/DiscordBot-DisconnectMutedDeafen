import asyncio
import discord
import os
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Conversion from sec to min
MIN = 5

client = discord.Client()

async def start():
    await retrieve_active_voice_channel()
 
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$kick'):
    await message.channel.send('Sempre no disconnect! A dar shades desde que o VG nasceu')

async def retrieve_active_voice_channel():
      """Scans all active voice channels the bot can see and returns one"""
      print("Here get channels")
      text_channel_list = []
      b = 1
      for guild in client.guilds:
          print(guild.voice_channels)
          for VoiceChannel in guild.voice_channels:
           # if len(channel.members) > 0:
              # We found an active voice channel!
              text_channel_list.append(VoiceChannel.name)
              print("increment:"+b)
              b = b + 1
              # xhannel = text_channel_list.append(channel)
              print(VoiceChannel.name)
@client.event
async def on_ready():
  print('This {0.user}'
  .format(client))
  while True:
      # Start the scheduler for a random time
      print("here 1")
      await asyncio.sleep(MIN)
      print("here 2")
      # Try to kick a user from a channel
      await start()
      print("here 3")

client.run(os.environ['token'])