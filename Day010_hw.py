# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""

import requests
# 引入函式庫
r = requests.get('https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html')
# 想要爬資料的目標網址
response = r.text
# 模擬發送請求的動作

fh = open("./day010_hw.txt", "w",encoding="utf-8")



from bs4 import BeautifulSoup

soup = BeautifulSoup(response, "html5lib")
print(soup,file=fh)
print( type(soup),"\n\n")
fh.close()




from grab import Grab
g = Grab()
resp = g.go('https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html')
resp.body

fh2 = open("./day010_hw2.txt", "w",encoding="utf-8")
from pyquery import PyQuery as pq
doc = pq(resp.body)

print(doc,file=fh2)
print(type(doc))


fh2.close()