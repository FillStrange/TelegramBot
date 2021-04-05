import requests
from bs4 import BeautifulSoup


url = 'https://ria.ru'
r = requests.get(url=url)
print(r.status_code)
html = BeautifulSoup(r.text, 'html.parser')

def hello ():
    for item in html.findAll('div', class_='cell-list__item m-no-image'):
        print('------------------------------')
        print('Заголовок: ', item.find('span', class_='cell-list__item-title').text)
        print('URL: ', item.find('a', class_='cell-list__item-link')['href'])
        return item.find('a', class_='cell-list__item-link')['href']