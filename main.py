import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from database import Data
import re

db = Data("datatext.db")


# show_alert=True

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6047593260:AAE3JLiErNQ0FUrNhH4lPp_umrTITeQ6rH8") #, proxy='http://proxy.server:3128'
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("ՀԱՐՑԵՐ")
    markup.add(button1)
    await message.reply(f'Բարև {message.from_user.first_name}, սեղմեք «ՀԱՐՑԵՐ» կոճակը:', reply_markup=markup)

@dp.message_handler(commands=["add"])
async def add_button(message: types.Message):
    try:
        pattern = r"\((.*?)\)"
        text = message.text
        maddern = re.findall(pattern, text)
        db.add_question(maddern[0], maddern[1])
        await message.answer("Գործողությունը հաջողությամբ ավարտվեց:")
    except Exception as e:
        await message.answer(f"Սխալ [{e}], խնդրում ենք կրկին փորձել:\nՀրամանի օրինակ - /add (հարց) (պատասխան)")

@dp.callback_query_handler()
async def callback(callback_query: types.CallbackQuery):
    question = db.select_question()
    buttons = [item[0] for item in question]
    if callback_query.data in buttons:
        quesans = db.select_question_answer(callback_query.data)
        ques_ans = [irem for irem in quesans]
        values = [irem for sublist in ques_ans for irem in sublist]
        await bot.send_message(callback_query.from_user.id, f"ՀԱՐՑ:\n{values[0]}\n\nՊԱՏԱՍԽԱՆ:\n{values[1]}")


@dp.message_handler()
async def pusto(message: types.Message):
    if message.text == "ՀԱՐՑԵՐ":
        voprosi = db.select_question()
        buttons = [item[0] for item in voprosi]

        max_buttons_per_page = 10  # Максимальное количество кнопок на одной странице
        total_pages = (len(buttons) - 1) // max_buttons_per_page + 1  # Общее количество страниц

        for page in range(total_pages):
            start_index = page * max_buttons_per_page
            end_index = start_index + max_buttons_per_page
            page_buttons = buttons[start_index:end_index]

            markup = InlineKeyboardMarkup()
            for item in page_buttons:
                markup.add(InlineKeyboardButton(item, callback_data=item))

            await message.answer(f"#{page + 1}", reply_markup=markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)