import os
from telegram import Bot

# pobieramy token i chat_id z GitHub Secrets
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Bot działa!")
