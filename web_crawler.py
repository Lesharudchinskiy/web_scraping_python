# В основе Веб-краулеров лежит рекурсия, он получает контент страницы по ее URL, исследует эту страницу, находит URL
# другой страницы, извлекает содержимое этой ДРУГОЙ страницы и так далее до бесконечности
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# стр 68 ...
