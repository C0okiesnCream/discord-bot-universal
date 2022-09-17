from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Bot as BotBase
from discord import Intents
from discord import Embed

from ..db import db

PREFIX = "+"
OWNER_IDS = [763257828391124992]

#add intents beneath this
intent = Intents.all()
intent.message_content = True
intent.presences = True
intent.messages = True
intent.dm_messages = True
intent.dm_reactions = True

class bot(BotBase):
 def __init__(self):
  self = self
  self.PREFIX = PREFIX
  self.ready = False
  self.guild = None
  self.scheduler = AsyncIOScheduler
  
  db.autosave(self.scheduler)
  super().__init__(
    command_prefix=PREFIX, 
    owner_ids=OWNER_IDS, 
    intents=intent
    )

 def run(self, version):
  self.VERSION = version

  with open("./library/bot/token.0", "r", encoding="utf-8") as tf:
   self.TOKEN = tf.read()

  print("running bot...")
  super().run(
    self.TOKEN, 
    reconnect=True
    )

 async def on_connect(self):
  print("bot connected")

 async def on_disconnect(self):
  print("bot disconnected")

 async def on_error(self, err, *args, **kwargs):
  if err == "on_command_error":
   await args[0].send("I did not get your request, please try again")

  raise

 async def command_error(self, ctx, exc):
  if isinstance(exc, CommandNotFound()):
   pass
  
  elif hasattr(exc, "original"):
   raise exc.original

 async def on_ready(self):
  if not self.ready:
   self.ready = True
   self.guild = self.get_guild(763258488415453216)
   self.scheduler.start()

   channel = self.get_channel(1019074854156255352)
   await channel.send("I am now here to tell you the Universe's secrets")

   embed = Embed(title="Universal is online", description="There are no commands yet lol", color=1752220)
   embed.set_image(url='https://spaceplace.nasa.gov/nebula/en/nebula1.en.jpg')
   embed.add_field(name="have fun with the no commands", value="lol, there are no commands to mess with, haha")
   embed.set_footer(text='Universal running: Alpha 0.2.2')
   embed.set_author(name='-C0okiesnCream', icon_url='https://64.media.tumblr.com/f237394f8295fcf59e7a7dde9b2986b3/e1ebdce54c2e4b04-ce/s1280x1920/284a18044baa7fa52293f3c2f694748b91ebb2b6.jpg')
   embed.set_thumbnail(url='https://www.sdxcentral.com/wp-content/uploads/2022/02/nebula.jpg')
   await channel.send(embed=embed)
   
   print('bot ready')

  else:
   print('bot connected')
 
 async def on_message(self, message):
  pass

Universal = bot()