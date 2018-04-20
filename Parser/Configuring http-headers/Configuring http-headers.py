from grab import Grab, UploadFile

import logging
logging.basicConfig(level=logging.DEBUG)
g = Grab()
#g.setup(headers={'Accept-Encoding': ''})
#g.go('http://digg.com')
#print(g.doc.headers.get('Content-Encoding'))
g.setup(headers={'Accept-Encoding': 'gzip'})
g.go('http://digg.com')
print(g.doc.headers['Content-Encoding'])