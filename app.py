# -*- coding: utf-8 -*

import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv('API_TOKEN')
FROM_CHATS = os.getenv('FROM_CHATS')
TO_CHAT = os.getenv('TO_CHAT')

chats = FROM_CHATS.split(",")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], content_types=types.ContentType.PHOTO)
async def group_handler(message: types.Message):
    if message.chat.username in chats:
        repost = await bot.forward_message(
          chat_id=f'@{TO_CHAT}',
          from_chat_id=message.chat.id,
          message_id=message.message_id
        )
    


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
