import asyncio
import discord
import os
import logging
import re
import datetime
import random

# from datetime import datetime
from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
now = datetime.datetime.now()
# Conversion from sec to min
MIN = 5

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = Bot("!")

link_list = ["https://media.giphy.com/media/l3V0j3ytFyGHqiV7W/giphy.gif", "https://media.giphy.com/media/63MO9LTRoTXQk/giphy.gif", "https://media.giphy.com/media/ikcJ56KAyhm8w/giphy.gif", "https://media.giphy.com/media/mFulmRSjkW9by/giphy.gif", "https://media.giphy.com/media/iNLyKccqVmiBy/giphy.gif", "https://media.giphy.com/media/kz6FtjoEVsNTlLnMXz/giphy.gif",
"https://media.giphy.com/media/bxd1GzWN0v7wY/giphy.gif", "https://media.giphy.com/media/2oeyTMKbIZsHK/giphy.gif", "https://media.giphy.com/media/kbQVMaf2s20f8gSKDm/giphy.gif"]
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
                  while re.search("self_mute=True self_deaf=True", str(strikes0)):
                  # if re.search("self_mute=True self_deaf=True", str(strikes0)):
                    print("kick")
                    await vkick(None,None,member)
                    # Still need to fix this as a indepedent config value
                    # right channel
                    channel = client.get_channel(863030632846589983)
                    # test channel
                    # channel = client.get_channel(797123135467814929)
                    embed = discord.Embed(title="Kick aos Teclas 3",description=str(member),color=0x9208ea,timestamp = now.utcnow())
                    embed.set_footer(text="Created by Komodoro")
                    embed.set_image(url=random.choice(link_list))
                    await channel.send(embed=embed)
                    return
              print("finish after this")

@client.event
async def on_ready():
  print('This {0.user}'
  .format(client))
  while True:
      # Start the scheduler for a random time
      print(discord.version_info)
      print(discord.__version__)
      print ("Current date and time : ")
      print (now.strftime("%Y-%m-%d %H:%M:%S"))
      print("here 1")
      await asyncio.sleep(MIN)
      print("here 2")
      # Try to kick a user from a channel
      await start()
      print("here 3")

client.run(os.environ['token'])