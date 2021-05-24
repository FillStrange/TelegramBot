from telebot import types

def start_buttons():#кнопки добавляются через запятую
   buttons = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
   return buttons.add('новости','мои подписки',)
