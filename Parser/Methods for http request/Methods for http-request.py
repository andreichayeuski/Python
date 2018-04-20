from grab import Grab, UploadFile

import logging
logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.setup(post={'act': 'login', 'redirec_url': '', 'captcha': '', 'login': 'root', 'password': '123'})
g.go('http://habrahabr.ru/ajax/auth/')
print(g.xpath_text('//title'))
g.setup(post={'login': 'root', 'password': '123'})
g.go('http://example.com/login')
g.go('http://example.com/news/recent')