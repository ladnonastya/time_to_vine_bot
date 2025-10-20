from datetime import datetime
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from constants import users, texts, drinks

#keyboard = InlineKeyboardMarkup()
#buttons = (InlineKeyboardButton(text=text, callback_data=drink) for text, drink in zip(texts, drinks))
#[keyboard.add(button) for button in buttons]

keyboard = InlineKeyboardMarkup(row_width=2,inline_keyboard=[[InlineKeyboardButton(text="грустненько :(", callback_data="vinishko")],
    [InlineKeyboardButton(text="хочу танцевать", callback_data="tequila")],
    [InlineKeyboardButton(text="тяжелый день, ваще жесть", callback_data="vodochka")],
    [InlineKeyboardButton(text="сегодня у меня пятница!", callback_data="viskarik")],
    [InlineKeyboardButton(text="у меня все хорошо", callback_data="rom")]])

def get_greetings():
    hour = int(datetime.now().hour)
    print(datetime.now())
    if 5 < hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 23:
        return "Доброго вечерочка"
    elif 23 <= hour or hour < 6:
        return "Доброй ночи"

def get_name(msg_or_query):
    if hasattr(msg_or_query, 'from_user'):
        username = msg_or_query.from_user.username
    else:
        username = msg_or_query.username
    return users.get(username, username or "друг")
