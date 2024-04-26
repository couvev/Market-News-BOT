from telegram import Bot
from telegram.constants import ParseMode
import os
from dotenv import load_dotenv

load_dotenv()


async def send(msg, url):
    bot = Bot(os.environ.get("TEL_BOT_KEY"))
    chat_id = '-1002005750638'
    await bot.send_photo(chat_id=chat_id, photo=url)
    await bot.send_message(chat_id=chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)
