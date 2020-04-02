# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Wikipedia爬蟲練習

@author: chenlw
"""

# 先複習一下原本純靜態的爬法

import time
from datetime import datetime

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

time.sleep(10)

for i in range(20):
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 10000);")

# 取得資料，丟到 BeautifulSoup 解析

html_source = browser.page_source
soup = BeautifulSoup(html_source, "html5lib")

for d in soup.find(class_="part_list_2").find_all('h3'):
    if (d.find(class_="date").text[0:10] == '2020/04/02'):
        print(d.find(class_="date").text, d.find_all('a')[-1].text)

# 關閉瀏覽器
browser.quit();

# 2. 取出現在時間兩小時內的新聞

for d in soup.find(class_="part_list_2").find_all('h3'):
    if (datetime.now()-datetime.strptime(d.find(class_="date").text, "%Y/%m/%d %H:%M")).seconds <= 7200 :
        print(d.find(class_="date").text, d.find_all('a')[-1].text)


## 3. 根據範例，取出三天前下午三點到五點的新聞
# 小改成  區間範圍(9-11點)

for d in soup.find(class_="part_list_2").find_all('h3'):
    if (d.find(class_="date").text[0:16] >= '2020/04/02 09:00') and (d.find(class_="date").text[0:16] <= '2020/04/02 11:00'):
        print(d.find(class_="date").text, d.find_all('a')[-1].text)





