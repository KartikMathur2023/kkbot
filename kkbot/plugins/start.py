
from .. import bot,openai_key
from telethon import events
import asyncio
import openai

openai.my_api_id=openai_key

@bot.on(events.NewMessage(incoming = True, pattern = "/start"))
async def start(event):
  await event.reply("Hello This is kkbot")
  


@bot.on(events.NewMessage(incoming = True, pattern = "/get"))
async def start(event):
  a=await event.reply("Hello This is Get command")
  await asyncio.sleep(3)
  await a.edit("This is edited message")
  
  
  
@bot.on(events.NewMessage(incoming = True, pattern = "/eval"))
async def start(event):
  await event.reply("Hello This is Eval command")
  
  

@bot.on(events.NewMessage(incoming = True, pattern = "/edit"))
async def start(event):
  a=await event.reply("Get command")
  await asyncio.sleep(3)
  await a.edit("This is edited message")