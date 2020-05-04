from datetime import datetime
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from constants import users, texts, drinks

keyboard = InlineKeyboardMarkup()
buttons = (InlineKeyboardButton(text=text, callback_data=drink) for text, drink in zip(texts, drinks))
[keyboard.add(button) for button in buttons]

def get_greetings():
    hour = int(datetime.now().hour)
    print
    if 5 < hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 23:
        return "Доброго вечерочка"
    elif 23 <= hour or hour < 6:
        return "Доброй ночи"

def get_name(msg):
    if users.get(msg.from_user.mention, None):
        return users[msg.from_user.mention]
    elif msg.from_user.mention == 'Илья Чистяков':
        return 'Илья Владимирович, самый лучший начальник'
    return 'друг'
