from grab import Grab, UploadFile

import logging

logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.setup(log_dir='log/grab')
g.go('http://yandex.ru', log_file='out.html')
g.setup(post={'hi': u'Превед, яндекс!'})
g.request()
