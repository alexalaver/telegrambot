import logging
from aiogram import Bot, types, Dispatcher, executor

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6047593260:AAE3JLiErNQ0FUrNhH4lPp_umrTITeQ6rH8")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)