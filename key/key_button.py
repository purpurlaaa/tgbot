from telebot import types
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton("Да"),
                                                               types.KeyboardButton("нет"))

keyboard2 = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Да", callback_data="yes"),
                                             types.InlineKeyboardButton("нет", callback_data="no"))