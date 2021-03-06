import asyncio
import discord
import os
import logging
import re
from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Conversion from sec to min
MIN = 5

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = Bot("!")

async def start():
    await retrieve_active_voice_channel()

@bot.command()
async def vkick(self, ctx, target_member: discord.Member):
    """Kicks a Member from a voice channel"""
    await target_member.move_to(None)
 
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
              # We found an active voice channel!
              print("Voice channel info:", VoiceChannel)
              text_channel_list.append(VoiceChannel.name)
              print("increment:", b)
              b = b + 1
              # print("print VoiceChannel Members", VoiceChannel.members)
              # xhannel = text_channel_list.append(channel)
              print("print Voice Channel Voice states", VoiceChannel.voice_states )
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
                  memberids = member.id
                  print("member:", member)
                  print("member id:", member.id)
                  print("member name:", member.name)
                  states = channel.voice_states
                  strikes = [states[memberids]]
                  strikes0 = strikes[0]
                  print(strikes0)
                  if re.search("self_mute=True self_deaf=True", str(strikes0)):
                    print("kick")
                    await vkick(None,None,member)
              print("finish after this")

@client.event
async def on_ready():
  print('This {0.user}'
  .format(client))
  while True:
      # Start the scheduler for a random time
      print(discord.version_info)
      print(discord.__version__)
      print("here 1")
      await asyncio.sleep(MIN)
      print("here 2")
      # Try to kick a user from a channel
      await start()
      print("here 3")

client.run(os.environ['token'])