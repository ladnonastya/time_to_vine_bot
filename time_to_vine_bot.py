import logging
import requests
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F
from random import randrange

from config import TOKEN, PATCHED_URL
from constants import greetings, buhat, drinks
from utils import get_name, get_greetings, keyboard

#setattr(api, "API_URL", PATCHED_URL)

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#@dp.message_handler(Text(equals=greetings, ignore_case=True))
@dp.message(F.text.lower().in_(greetings))
async def greet(msg):
    greeting = get_greetings()
    user = get_name(msg)
    await msg.answer(f"{greeting}, {user}")
    await msg.answer('Как твои дела сегодня?', reply_markup=keyboard)


#@dp.message_handler(Text(equals=buhat, ignore_case=True))
@dp.message(F.text.in_(buhat))
async def send(msg):
    user = get_name(msg)
    await msg.answer('ну го, чё')
    await msg.answer_photo("http://picscomment.com/pics/3690.jpg")
    await msg.answer('Как твои дела сегодня?', reply_markup=keyboard)


@dp.callback_query(F.data.in_(drinks))
async def mood_callback(query):
    data = query.data
    if data == 'vinishko':
        await bot.send_message(query.from_user.id, f'я думаю, что тебе нужно винишко, {get_name(query)}')
        await bot.send_message(query.from_user.id, 'смотри, что я для тебя нашел - https://edadeal.ru/moskva/offers?segment=wine')
    elif data == 'tequila':
        await bot.send_message(query.from_user.id, 'для тебя сейчас самое оно - текила!')
        await bot.send_message(query.from_user.id, 'тут короче есть скидоны - https://edadeal.ru/moskva/offers?segment=tequila')
    elif data == 'vodochka':
        await bot.send_message(query.from_user.id, 'сочувствую')
        await bot.send_message(query.from_user.id, 'вот тут глянь, может что поможет - https://edadeal.ru/moskva/offers?segment=vodka')
    elif data == 'viskarik':
        await bot.send_message(query.from_user.id, 'у меня есть кое-что для тебя')
        await bot.send_message(query.from_user.id, 'даже скидочка есть - https://edadeal.ru/moskva/offers?segment=whiskey')
        await bot.send_message(query.from_user.id, f'{get_name(query)}, только не забудь взять колу')
    elif data == 'rom':
        await bot.send_message(query.from_user.id, 'ну вот и отлично! сейчас будет еще лучше')
        await bot.send_message(query.from_user.id, 'хорошего вечера тебе')
        await bot.send_message(query.from_user.id,'https://edadeal.ru/moskva/offers?segment=other-alcohols')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logger.info("Запускаю бота...")
    asyncio.run(main())


# если проблемы с getUpdates - удалить вебхуки по урлу:
# https://api.telegram.org/bot487294417:AAHGPK8puACx7ilbHkQAWSAZoEaBkeS6J9w/deleteWebhook