from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLink(pageUrl):
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:  # Проверяем есть ли href в словаре атрибутов
            if link.attrs['href'] not in pages: # Выбирает значения ключа href в словаре атрибутов
                # Мы нашли новую страницу
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLink(newPage)


getLink('')
# Страница 80

