from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Intents

PREFIX = "+"
OWNER_IDS = [763257828391124992]

#add intents beneath this
intent = Intents.default()

class bot(BotBase):
 def __init__(self):
  self = self
  self.PREFIX = PREFIX
  self.ready = False
  self.guild = None
  self.scheduler = AsyncIOScheduler

  super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=intent)

 def run(self, version):
  self.VERSION = version

  with open("./library/bot/token.0", "r", encoding="utf-8") as tf:
   self.TOKEN = tf.read()

  print("running bot...")
  super().run(self.TOKEN, reconnect=True)

 async def on_connect(self):
  print("bot connected")

 async def on_disconnect(self):
  print("bot disconnected")
  
 async def on_ready(self):
  if not self.ready:
   self.ready = True
   self.guild = self.get_guild(763258488415453216)
   print("bot ready")

  else:
   print('bot connected')
 
 async def on_message(self, message):
  pass

Universal = bot()