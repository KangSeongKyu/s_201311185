#!/usr/bin/env python
# coding: utf-8

import requests
import lxml.html
from lxml.cssselect import CSSSelector

re = requests.get('https://www.tiobe.com/tiobe-index/');
html = lxml.html.fromstring(re.text)

sel1 = CSSSelector('body > section > section > section > article > table.table.table-striped.table-top20 > tbody > tr:nth-child(n) > td:nth-child(1)')
sel2 = CSSSelector('body > section > section > section > article > table.table.table-striped.table-top20 > tbody > tr:nth-child(n) > td:nth-child(4)')
sel3 = CSSSelector('body > section > section > section > article > table.table.table-striped.table-top20 > tbody > tr:nth-child(n) > td:nth-child(5)')

nodes1 = sel1(html)[:20]
nodes2 = sel2(html)[:20]
nodes3 = sel3(html)[:20]
print u"<<1. TIOBE 사이트 프로그래밍 언어 순위 크롤링>>\n"
print "Ranking".ljust(10), "Languages".ljust(20), "Rating".ljust(10)
print "----------------------------------------"
for i in range(0, len(nodes1)):
    print nodes1[i].text.ljust(10),nodes2[i].text.ljust(20),nodes3[i].text.ljust(10)
print '\n'
#################################################################################################

print u"<<2. 사람인 사이트 open api읽기>>\n"
import urlparse
import os
import requests
import re
import StringIO

import lxml.etree
import xml.etree.ElementTree as ET
search = []
lang = []
for total in range(0,len(nodes1)):
    print u"프로그래밍 언어: ", nodes2[total].text
    lang.append(nodes2[total].text)
    LANG = nodes2[total].text
    SERVICE = 'job-search?'
    KEYWORDS = 'keywords='
    CATEGORY = 'job_category=401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416'
    params=os.path.join(SERVICE+KEYWORDS+LANG+'&'+CATEGORY)

    _url='http://api.saramin.co.kr/'
    url=urlparse.urljoin(_url,params)

    data=requests.get(url).text
    tree=ET.fromstring(data.encode('utf-8'))
    std = tree.find('jobs')
    ttl = std.get('total')
    search.append(int(ttl))
    print u"채용정보 검색 수: ",ttl
    p=re.compile('<title>(.+?)</title>')
    res=p.findall(data)
    for item in res:
        print item
    print '\n'
##############################################################################################################
import matplotlib.pyplot as plt

data = search
labels = lang
#def barchart(data, labels):
print u"3. 프로그래밍 언어 별 채용 검색 수 그래프"
num_bars = len(data)
positions = range(1, num_bars + 1)
plt.barh(positions, data, align='center')
plt.yticks(positions, labels)
plt.xlabel('Total Searchs')
plt.ylabel('Programming Languages')
plt.title('Each PLs Total Searchs')
plt.grid()
plt.show()
#if __name__ == "__main__":
#    barchart(search, lang)