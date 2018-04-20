from grab import Grab
import logging

logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.go('http://habrahabr.ru')
g.xpath('//h2/a[@class="topic"]').get('href')

print(g.xpath_text('//h2/a[@class="topic"]'))
print(g.css_text('h2 a.topic'))
print('Comments:', g.css_number('.comments .all'))
from urllib.parse import urlsplit

print(', '.join(urlsplit(x.get('href')).netloc for x in g.css_list('.hentry a') if
                not 'habrahabr.ru' in x.get('href') and x.get('href').startswith('http:')))
