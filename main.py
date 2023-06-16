import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# show_alert=True

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6047593260:AAE3JLiErNQ0FUrNhH4lPp_umrTITeQ6rH8", proxy='http://proxy.server:3128')
dp = Dispatcher(bot)

@dp.callback_query_handler()
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == 'show_notification':
        await bot.answer_callback_query(callback_query.id, text='Текст уведомления', show_alert=True)

@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Показать уведомление', callback_data='show_notification')
    keyboard.add(button)
    await message.reply('Нажмите кнопку, чтобы показать уведомление', reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)