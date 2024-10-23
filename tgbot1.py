from telebot import types, TeleBot
from dotenv import load_dotenv
import os
bot = TeleBot('7722176687:AAEMdlgdfRPzPExPmub2SFqXt9eGRqz1f0c')

@bot.message_handler(commands=['start'])
def get_start(message):
    bot.send_message(message.from_user.id, 'Напиши привет')

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Привет друг")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, 'я тебя не понимаю напиши /help')


bot.polling(none_stop= True)
    