import telebot
import config
import requests
from telebot import TeleBot, types
from telebot import types
from jokes_bot import get_joke, update_joke
from news_bot import send_news

TOKEN = config.TOKEN

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Анекдот')
    itembtn2 = types.KeyboardButton('Новости')

    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот, который может рассказать анекдот или показать новости.\nВыберите что вам нужно:".format(
                         message.from_user, bot.get_me()),
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Анекдот')
def send_joke_handler(message):
    bot.send_message(message.chat.id, get_joke())

@bot.message_handler(func=lambda message: message.text == 'Новости')
def send_news_handler(message):
    news = requests.get('https://dzen.ru/').text
    send_news(bot, message.chat.id)


bot.polling(none_stop=True)
