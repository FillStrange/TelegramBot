import telebot

bot = telebot.TeleBot('1666647830:AAFsDD9zFq5esH7QLTPANc1lrDNXm3DEiOs')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Агрегатор новостей! Здесь вы можете подписаться на рассылку '
                                      'интересующих вас новостей, которые бот будет ежедневно вам отправлять.'
                                      'Для справок напишите команду /help')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '')

@bot.message_handler(commands=['news'])
def send_text(message):

    bot.polling()