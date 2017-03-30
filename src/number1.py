import requests
rResponse = requests.get('http://python.org/')
_html = rResponse.text
print len(_html)

import requests
rResponse = requests.get('http://python.org/')
_html = rResponse.text
print len(_html)

print type(_html)

print rResponse.headers

print uResponse.info()