import telebot
from bs4 import BeautifulSoup
import requests
bot = telebot.TeleBot("1698226925:AAEcOzVmnyYOHhydN31PwBmO_oHKx9AZnNc")
url = 'https://www.afisha.ru/chelyabinsk/schedule_concert/'
page = requests.get(url)

key_default = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_default.row(types.KeyboardButton('Button 1'))

@bot.message_handler(func=lambda message: messages.text == u'Button 1') #Если была вызвана Button 1
#Тут пишем метод который будет выполнятся, когда нажмём на кнопку
def button(message):
     bot.send_message('Тут надо вписать id чата', 'Сюда пишем текст типо - Привет')

# Парсим страницу
 
soup = BeautifulSoup(page.text, 'html.parser')
events = soup.findAll('li', class_='SlE6Y _1gSmu')
 
# Собираем необходимые данные со страницы:

answer = ''
for i in events:
    event = i.find('section').find('h3').find('a').get_text()
    try:
        desc = i.find('section').find('div', class_='').get_text()
    except:
        desc = "Нет описания"
    date = i.find('section').find('div', class_='_1Jo7v').get_text()

    answer += event + desc + date + '\n\n'

print(answer)
 
# Отправляем через бота:
 
@bot.message_handler(content_types=['text'])
def send_events_chel(message):
        bot.send_message(message.chat.id, answer)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "shop":
        shop = telebot.types.InlineKeyboardMarkup();
        product = telebot.types.InlineKeyboardButton(text='Чай Greenfield', callback_data='tea');
        shop.add(product);
    elif call.data == "tea":
        bot.send_message(call.message.chat.id, 'Вы выбрали чай гринфилд!');


bot.polling(none_stop=True)