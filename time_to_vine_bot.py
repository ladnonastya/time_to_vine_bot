import requests  
import datetime
import telebot
from telebot import types
from telebot import apihelper

token = '487294417:AAHGPK8puACx7ilbHkQAWSAZoEaBkeS6J9w'

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=2):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None
        return last_update
    
        
greet_bot = BotHandler(token)  
greetings = ('здравствуй', 'привет', 'ку', 'здорово', 'здравствуйте', 'дратути')  
now = datetime.datetime.now()


def main():  
    new_offset = None
    today = now.day
    hour = now.hour
    
    m = types.InlineKeyboardMarkup()
    m.add(types.InlineKeyboardButton(text = 'грустненько', callback_data='vinishko'))
    m.add(types.InlineKeyboardButton(text = 'хочу танцевать', callback_data='tequila'))
    
    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        if isinstance(last_update, list): 
            last_update_id = last_update[-1]['update_id'] 
        elif last_update == None: 
            continue 
        else: 
            last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Доброго вечерочка, {}'.format(last_chat_name))
            #today += 1
            
        elif last_chat_text.lower() in greetings and today == now.day and (23 <= hour or hour < 6) :
            greet_bot.send_message(last_chat_id, 'Доброй ночи, {}'.format(last_chat_name))

        elif last_chat_text.lower()=='го бухать' or last_chat_text.lower()=='го бухать?' or last_chat_text.lower()=='го бухать!':
            #greet_bot.send_message(last_chat_id, 'Го')
            apihelper.send_photo(token,last_chat_id,'http://picscomment.com/pics/3690.jpg')
            
		
		
		apihelper.send_message(token, last_chat_id, 'Как твои дела сегодня?', reply_markup = m)
		
		new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()

