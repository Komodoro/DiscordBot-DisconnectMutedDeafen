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
          print(guild)
          print("space - guilds")
          print(guild.members)
          print(guild.voice_channels)
          #if isinstance(channel, discord.VoiceChannel):
          #  if len(channel.members) > 0:
                # We found an active voice channel!
          for VoiceChannel in guild.voice_channels:
           # if len(channel.members) > 0:
              # We found an active voice channel!
              text_channel_list.append(VoiceChannel.name)
              print("increment:", b)
              b = b + 1
              print(VoiceChannel.members)
              # xhannel = text_channel_list.append(channel)
              print(VoiceChannel.voice_states )
              print("channel id")
              channel = client.get_channel(VoiceChannel.id) 
              print("print channel name",channel.name)
              #gets the channel you want to get the list from
              print("associate members in specific channel")
              members = channel.members #finds members connected to the channel
              print(members)
              memids = [] #(list)
              print("print the members id's")
              for member in members:
                  memids.append(member.id)
              print(memids) #print info
              print("finish after this")
              #for members in VoiceChannel.members
              #  print(members)
      
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