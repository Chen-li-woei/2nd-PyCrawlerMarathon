# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Wikipedia爬蟲練習

@author: chenlw
"""

# 先複習一下原本純靜態的爬法

import requests
from bs4 import BeautifulSoup

url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

for d in soup.find(class_="part_list_2").find_all('h3'):
    print(d.find(class_="date").text, d.find_all('a')[-1].text)

# 打開瀏覽器

from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome(executable_path='chromedriver')

browser.get("https://www.ettoday.net/news/news-list.htm")




# 每個兩秒鐘自動往下滑

import time
for i in range(10):
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 10000);")

# 取得資料，丟到 BeautifulSoup 解析

html_source = browser.page_source
soup = BeautifulSoup(html_source, "html5lib")

for d in soup.find(class_="part_list_2").find_all('h3'):
    print(d.find(class_="date").text, d.find_all('a')[-1].text)

# 關閉瀏覽器
browser.quit();










