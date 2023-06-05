from telethon import TelegramClient
import logging
import time

openai_key = "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"
api_id = "27611929"
api_hash = "dfce0eee21543a8992e360a2ece1269f"
bot_token = "6191885401:AAGBsSO38iCILeiVXsi9cIsQmV6yBkUSiaM" 

bot = TelegramClient("kkbot", api_id,api_hash).start(bot_token = bot_token)