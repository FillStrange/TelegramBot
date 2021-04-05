import requests
from bs4 import BeautifulSoup


url = 'https://3dnews.ru/gadgets/rss/'
r = requests.get(url=url)
print(r.status_code)

xml = BeautifulSoup(r.text, 'xml')
items = xml.findAll('item')
print(len(items))


def pcnews():
    for item in items:
        print('------------------------------')
        print('Заголовок: ', item.find('title').text)
        print('URL: ', item.find('link').text)
        print('data: ', item.find('pubDate').text)
        return item.find('link').text