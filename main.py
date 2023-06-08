import logging
import MySQLdb
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6047593260:AAE3JLiErNQ0FUrNhH4lPp_umrTITeQ6rH8", proxy='http://proxy.server:3128')
dp = Dispatcher(bot)


connect = MySQLdb.connect(
    user='AlexMan04',
    password='qbc679898',
    host='AlexMan04.mysql.pythonanywhere-services.com',
    database='tgbot',
)

cursor = connect.cursor()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = KeyboardButton(text='Заработать деньги')
    button2 = KeyboardButton(text='Профиль')
    markup.add(button1, button2)
    await message.answer("Привет", reply_markup=markup)

@dp.message_handler()
async def classic(message: types.Message):
    if message.text == "Заработать деньги":
        await message.answer("+1 рубль")
    elif message.text == "Профиль":
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        await message.answer(result)


connect.close()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)