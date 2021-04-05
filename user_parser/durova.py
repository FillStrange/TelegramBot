import requests
from bs4 import BeautifulSoup


url = 'https://kod.ru/tag/news/rss/'
r = requests.get(url=url)
print(r.status_code)

xml = BeautifulSoup(r.text, 'xml')
items = xml.findAll('item')
print(len(items))

def dur():
    for item in items:
        print('------------------------------')
        print('Заголовок: ', item.find('title').text)
        print('URL: ', item.find('link').text)
        print('data: ', item.find('pubDate').text)
        return item.find('link').text