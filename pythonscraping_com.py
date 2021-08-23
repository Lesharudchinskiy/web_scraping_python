from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')  # html.read() - получаем контент страницы в
# формате HTML, 'html.parser' - синтаксический анализатор BeautifulSoup
name_list = bs.find_all('span', {'class': {'green', 'red'}})  # Функция find_all() - помогает
# извлечь все имена , путем выбора текста из тегов 'span', {'class': 'green'}
# Синтаксис  :     bs.find_all(имяТега,атрибутыТега) или find(tag, attributes) или
# .find_all(['h1','h2','h3','h4','h5','h6'])
for name in name_list:
    print(name.get_text())  # переменная.get_text() - функция очистки контента от тегов, она удаляет из
    # документа все теги. Данная функция должна быть последней , перед выводом готовых данных.



# page 43 ...