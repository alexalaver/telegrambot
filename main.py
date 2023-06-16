import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# show_alert=True

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6047593260:AAE3JLiErNQ0FUrNhH4lPp_umrTITeQ6rH8", proxy='http://proxy.server:3128')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    markup = ReplyKeyboardMarkup()
    button1 = KeyboardButton("ՀԱՐՑԵՐ")
    markup.add(button1)
    await message.reply(f'Բարև {message.from_user.first_name}, սեղմեք «ՀԱՐՑԵՐ» կոճակը:', reply_markup=markup)

@dp.message_handler()
async def pusto(message: types.Message):
    if message.text == "ՀԱՐՑԵՐ":
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("Մագնիսական փոխազդեցություն էրստեդի Ամպերի փորձերը։ Մագնիսական դաշտ Մագնիսական դաշտի ինդուկցիայի վեկտորը: Մագնիսական ինդուկցիայի գծեր, դրանց հատկությունները: Վերադրման սկզբունքը մագնիսական դաշտի համար", callback_data="harc1")
        markup.add(button1)
        await message.reply("Ահա բոլոր հարցերը:", reply_markup=markup)


@dp.callback_query_handler()
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == 'harc1':
        await bot.answer_callback_query(callback_query.id, text='Текст уведомления', show_alert=True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)