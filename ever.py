import telebot
import mysql.connector
from telebot import types
from user_parser import ria
from user_parser import nn
from user_parser import durova
from user_parser import play
from user_parser import habr
from user_parser import lenta
from user_parser import auto
from user_parser import pc

bot = telebot.TeleBot('1698226925:AAEcOzVmnyYOHhydN31PwBmO_oHKx9AZnNc')


cnx = mysql.connector.connect(user='root', password='123',
                               host='127.0.0.1',
                               database='bot')

cnx.close()


@bot.message_handler(commands=['news'])
def start(m):
    keyboard = types.InlineKeyboardMarkup()  #Клавиатура

    a = [["Риа новости (СМИ)", "yes"], ["Новости НН (СМИ)", "nn"], ["Код Дурова (СМИ)", "mo"], ["Playground (Игры)", "po"], ["Habr (Наука)", "go"], ["Лента ру (СМИ)" , "le"],
         ["Авто (Технологии)", "au"], ["ПК (Технологии)", "pc"]]

    for res in a:
        keyboard.add(types.InlineKeyboardButton(text=res[0], callback_data=res[1]))

    question = 'Выберете новостные порталы:'
    bot.send_message(m.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, ria.hello())
    elif call.data == "nn":
        bot.send_message(call.message.chat.id, nn.nn())
    elif call.data == "mo":
        bot.send_message(call.message.chat.id, durova.dur())
    elif call.data == "po":
        bot.send_message(call.message.chat.id, play.pgd())
    elif call.data == "go":
        bot.send_message(call.message.chat.id, habr.habr())
    elif call.data == "le":
        bot.send_message(call.message.chat.id, lenta.lenta_ru())
    elif call.data == "au":
        bot.send_message(call.message.chat.id, auto.auto())
    elif call.data == "pc":
        bot.send_message(call.message.chat.id, pc.pcnews())
    bot.clear_step_handler(call.message)

bot.polling(none_stop=True, interval=0)