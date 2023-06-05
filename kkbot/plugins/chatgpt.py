from telethon import events
from .. import bot
import asyncio
import openai
openai_key  = "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"
openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern="(?i)/ask"))
async def chatgpt(event):
  if event.sender_id == int("5687473991"):
   await event.reply("You have started kkbot")
  else:
   await event.reply("Nice to see you all 😊")