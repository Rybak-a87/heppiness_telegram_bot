from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio

from config import bot_TOKEN
from soul import *


bot = Bot(bot_TOKEN)
dp = Dispatcher(bot)


# обработка команды /start
@dp.message_handler(commands=["start"])
async def com_start(msg: types.Message):
    await asyncio.sleep(1)
    await bot.send_photo(msg.from_user.id, photo, HELLO)


# обработка входящего сообщения
@dp.message_handler()
async def dialog(msg: types.Message):
    user_id = msg.from_user.id
    msg_to_file(user_id, msg.text)
    await asyncio.sleep(1)
    if check(coincidence, msg.text.lower()):
        await bot.send_message(user_id, out_gen(answer))
        await asyncio.sleep(random.randint(8, 9))
        await bot.send_message(user_id, out_gen(answer))
    else:
        await msg.reply(miss_msg())


# запуск бота
if __name__ == "__main__":
    executor.start_polling(dp)
