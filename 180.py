from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('7138532568:AAEs-Lx4F0FRgn53lL0tnT3vFoYr-FWfBaw')
dp = Dispatcher(bot)

@dp.message_handler(commands=['Start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть сайт', web_app=WebAppInfo(url="https://mr-1-19.github.io/")))
    await message.answer('Hi', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message:types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(message.web_app_data.data)
    await message.answer(f'Имя {res["name"]}, Почта: {res["email"]}')

executor.start_polling(dp)