import asyncio
import logging  # Add logging capability
from telegram import Bot
from telegram.error import TelegramError


async def send_msg(token, chat_id, msg: str):
    try:
        bot = Bot(token)
        await bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML')
        print("Message sent")

    except TelegramError as error:
        print(f'Telegram Bot Fails to Alert. Error:\n{error}')

def send_telegram_message(text_message:str):

    token = "5955725734:AAHB8OJup3aq4Wqt6_3GtO634DMrZ5lF5Mo" 
    chat_id = -977791565
    msg = text_message

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(send_msg(token, chat_id, msg))
    except asyncio.TimeoutException:
        loop.close()