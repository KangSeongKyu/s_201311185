import urllib
import re
uResponse = urllib.urlopen('http://python.org/')
_html = uResponse.read()
#p=re.compile('http://.+"')
p=re.compile('href="(http://.*?)"')
nodes=p.findall(_html)
print "python.org 페이지를 크롤링해서 http url 출력하기"
print len(nodes)
for i, node in enumerate(nodes):
    print i, node