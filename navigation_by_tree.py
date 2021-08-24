# Объекты BeautifulSoup:
# 1) Объекты BeautifulSoup - экземпляры, которые встречались в виде переменной bs
# 2) Объекты Tag - в виде списков или отдельных элементов, как результат ф-ии find и find_all для
# объекта BeautifulSoup или полученные при проходе по структуре объекта BeautifulSoup: bs.div.h1
# 3) Объекты NavigableString - служат для представления не самих тегов, а текста внутри тегов
# 4) Объекты Comment - применяются для поиска HTML - комментариев, заключенных в теги комментариев <!--
# например,так-->

# Поиск тега по расположенияю в документе: bs.tag.subTag.anotherSubTag

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
# Получить только тех потомков, которые являются детьми, можно с помощью генератора .children:
# генератора .descendants - вывести потомков, не являющимися детьми
# for child in bs.find('table', {'id': 'giftList'}).children:
#   print(child)
# .next_siblings - упрощает сбор данных из таблиц, особенно, если есть заголовки (исключает заголовки таблиц)
# siblings - братья и сестры, сам объект не включается (tr - исключается)
# .previous_siblings -  если в конце списка легко выбираемый тег
# .next_sibling и .previous_sibling - для выбора одного тега, а не списка всех доступных
# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#    print(sibling)
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# page 54 ...
