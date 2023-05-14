import requests
from bs4 import BeautifulSoup

def send_news(bot, chat_id):
    URL = "https://dzen.ru/"
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'html.parser')

    news = []
    for i in soup.find_all('a', class_='card-image-view__clickable'):
        news.append(i['href'])

    if news:
        for article in news[:5]:
            bot.send_message(chat_id, article)
    else:
        bot.send_message(chat_id, 'К сожалению, новостей не найдено.')

