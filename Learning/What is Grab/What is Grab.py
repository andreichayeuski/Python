from grab import Grab, UploadFile

import logging

logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.setup(log_dir='log/grab')
g.go('https://afisha.tut.by/film/', log_file='out.html')
g.setup(post={'hi': u'Превед, яндекс!'})
g.request()
