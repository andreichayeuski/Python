from grab import Grab
import re
import logging

logging.basicConfig(level=logging.DEBUG)

g = Grab()
g.go('http://habrahabr.ru')
g.search(u'Google')
g.search(u'яндекс')
g.search(u'Яндекс')
g.search(u'гугл')
g.search(u'Медведев')
g.search('Медведев')
g.search('Медведев', byte=True)
g.search_rex(re.compile('Google'))
g.search_rex(re.compile('Google\s+\w+', re.U))

g.assert_substring('скачать торрент бесплатно')
g.assert_substring(u'скачать торрент бесплатно')
g.drop_spaces('foo bar')
g.drop_space('foo bar')
g.normalize_space(' foo \n \t bar')
g.find_number('12 человек на сундук мертвеца')
