from telebot import types, TeleBot
from key_button import keyboard

bot = TeleBot('7722176687:AAEMdlgdfRPzPExPmub2SFqXt9eGRqz1f0c')


@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    bot.send_message(call.message.chat.id, f'вы нажали {call.data}')

@bot.message_handler(commands=['start'])
def get_start(message):
    bot.send_message(message.from_user.id, 'привет', reply_markup=keyboard)

bot.polling(non_stop=True)