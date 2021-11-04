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
bot = Bot(command_prefix="$")

link_list = ["https://media.giphy.com/media/l3V0j3ytFyGHqiV7W/giphy.gif", "https://media.giphy.com/media/63MO9LTRoTXQk/giphy.gif", "https://media.giphy.com/media/ikcJ56KAyhm8w/giphy.gif", "https://media.giphy.com/media/mFulmRSjkW9by/giphy.gif", "https://media.giphy.com/media/iNLyKccqVmiBy/giphy.gif", "https://media.giphy.com/media/kz6FtjoEVsNTlLnMXz/giphy.gif",
"https://media.giphy.com/media/bxd1GzWN0v7wY/giphy.gif", "https://media.giphy.com/media/2oeyTMKbIZsHK/giphy.gif", "https://media.giphy.com/media/kbQVMaf2s20f8gSKDm/giphy.gif"]
async def start():
    await retrieve_active_voice_channel()

@bot.command()
async def vkick(self, ctx, target_member: discord.Member):
    """Kicks a Member from a voice channel"""
    await target_member.move_to(None)

@bot.command()
async def bot_join(ctx, *, channel: discord.VoiceClient = None): # TAKING ARGUMENT CHANNEL SO PPL CAN MAKE THE BOT JOIN A VOICE CHANNEL THAT THEY ARE NOT IN
    """Joins a voice channel."""
    destination = channel
    await destination.connect() # CONNECTING TO DESTINATION
    # await ctx.send(f"Succesfully joined the voice channel: {destination.name} ({destination.id}).")

#@client.command(name='join',aliases = ['summon']) # CREATING COMMAND "JOIN" WITH ALIAS SUMMON
#async def bot_join(ctx, *, channel: discord.VoiceChannel = None): # TAKING ARGUMENT CHANNEL SO PPL CAN MAKE THE BOT JOIN A VOICE CHANNEL THAT THEY ARE NOT IN
   # """Joins a voice channel."""
   # destination = channel if channel else ctx.author.voice.channel # CHOOSING THE DESTINATION, MIGHT BE THE REQUESTED ONE, BUT IF NOT THEN WE PICK AUTHORS VOICE CHANNEL
   # if ctx.voice_client: # CHECKING IF THE BOT IS PLAYING SOMETHING
       # await ctx.voice_state.voice.move_to(destination) # IF THE BOT IS PLAYING WE JUST MOVE THE BOT TO THE DESTINATION
   #     return

   # await destination.connect() # CONNECTING TO DESTINATION
   # await ctx.send(f"Succesfully joined the voice channel: {destination.name} ({destination.id}).")
 
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$kick'):
    await message.channel.send('Sempre no disconnect! A dar shades desde que o VG nasceu')

@bot.command(name="join")
async def join(ctx):
    author = ctx.message.author
    channel = author.voice.channel
    await channel.connect()
    print("i'm in the voice channel")


@bot.command(name="leave")
async def leave(ctx):
    await ctx.voice_client.disconnect()
    print("i'm out of the voice channel")


#@bot.command(name="join")
#async def join(ctx):
#    channel = ctx.author.voice.channel
#    voice = get(self.bot.voice_clients, guild=ctx.guild)
#    if voice and voice.is_connected():
#        await voice.move_to(channel)
#    else:
#        voice = await channel.connect()
#@bot.command(name="leave")
#async def leave(ctx):
#    await ctx.voice_client.disconnect()

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
              channel = client.get_channel(VoiceChannel.id) 
              print("print channel id",channel.id)
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
                  print("channel id:", channel.id)
                  print("channel name:", channel.name)
                  # print("bot name:", client.name)
                  # print("bot id:", client.id)
                  states = channel.voice_states
                  strikes = [states[memberids]]
                  strikes0 = strikes[0]
                  print(strikes0)
                  while re.search("self_mute=True self_deaf=True", str(strikes0)):
                  # if re.search("self_mute=True self_deaf=True", str(strikes0)):
                    #await bot_join(channel.id)
                    #print('Bot joined the channel.')
                    #voice = channel.id
                    # bot.connect(channel.id)
                    #xclientconnect = channel.id
                    #await xclientconnect.move_to()
                    # channel.id.move_to()
                    #{.author}
                    #await join(member)
                    print("kick")
                    await vkick(None,None,member)
                    # user = client.get_user(memberids)
                    #await user.send('Olá, foste kickado por estares Deafen. Estás a ser alvo de uma experiencia social')
                    # Still need to fix this as a indepedent config value
                    # right channel
                    channelget = client.get_channel(863030632846589983)
                    # test channel
                    # channel = client.get_channel(797123135467814929)
                    embed = discord.Embed(title="Kick aos Teclas 3",description=str(member)+" | "+ str(member.nick),color=0x9208ea,timestamp = now.utcnow())
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(text="Do: "+str(channel))
                    embed.set_image(url=random.choice(link_list))
                    await channelget.send(embed=embed)
                    #await xclientconnect.voice_client.disconnect()
                    #await leave()
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