from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')  # html.read() - получаем контент страницы в
# формате HTML, 'html.parser' - синтаксический анализатор BeautifulSoup
# СОЗДАМ ЭКЗЕМПЛЯР :
name_list = bs.find_all('span', {'class': {'green', 'red'}})  # Функция find_all() - помогает
# извлечь все имена , путем выбора текста из тегов 'span', {'class': 'green'}
# Синтаксисы  :    .find_all(tag, attributes, recursive, text, limit, keywords)
#                  .find(tag, attributes, recursive, text, keywords)
# .find_all(['h1','h2','h3','h4','h5','h6']) - можно подать список (он работает как OR)
# .find_all(text='the prince') - можно подать текст
# Аргумент recursive=True - по умолчанию, чтобы искать в дочерних элементах и потомках
# Аргумент limit - ограничить поиск первых n элементов
# Аргумент keyword - позволяет выбрать теги, содержащие определенный атрибут или набор атрибутов,
# пример: title = bs.find_all(id='title', class_='text')
for name in name_list:
    print(name.get_text())  # переменная.get_text() - функция очистки контента от тегов, она удаляет из
    # документа все теги. Данная функция должна быть последней , перед выводом готовых данных.
name_list_prince = bs.find_all(text='the prince')
print(len(name_list_prince))



# page 46 ...
