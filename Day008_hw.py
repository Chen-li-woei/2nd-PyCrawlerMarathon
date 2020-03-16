# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""
import requests
# 引入函式庫
r = requests.get('https://github.com/timeline.json')
# 想要爬資料的目標網址
response = r.text
# 模擬發送請求的動作

####下列為字串
# print(response)
# response['message']
# print(type(response))

# # print(response['message'])
# print(response[:100])

###########
import json
response = json.loads(response)

print(type(response))
print(response['message'])


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

print(html_doc)
print(type(html_doc))

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html5lib")
print(soup)
print(type(soup))