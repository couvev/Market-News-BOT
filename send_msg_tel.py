from telegram import Bot
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()


async def send(msg, title, link_url):
    try:
        bot = Bot(os.environ.get("TEL_BOT_KEY"))
        chat_id = '-1002005750638'
        message = f"{title}\n\n{msg}\n\nSaiba mais: {link_url}"
        await bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        raise e

if __name__ == "__main__":
    pass
