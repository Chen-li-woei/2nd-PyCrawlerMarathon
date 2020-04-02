# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Ettoday 網路爬蟲實作練習
能夠利用 selenium + BeatifulSoup 撰寫爬蟲，並存放到合適的資料結構

作業目標
根據範例：

取出今天所有的新聞
取出現在時間兩小時內的新聞
根據範例，取出三天前下午三點到五點的新聞


@author: chenlw
"""

# 1. 根據範例，取出今天所有的新聞

from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome(executable_path='chromedriver')

browser.get("https://www.ettoday.net/news/news-list.htm")

# 取得昨天時間
from datetime import datetime, timedelta
date_time = datetime.now() - timedelta(1)
date_time = date_time.strftime("%Y/%m/%d")
print("取得昨天時間：", date_time)

# 利用 selenium 持續執行下滑的動作，直到取得「昨天時間」的新聞，表示今天的已經取得完畢
import time
while True:
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(2)
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "html5lib")
    print(soup.find_all(class_="part_list_2")[-1].find_all('h3')[-1].find(class_="date").text)
    if date_time in soup.find_all(class_="part_list_2")[-1].find_all('h3')[-1].find(class_="date").text:
        print('==== STOP ====')
        break

# 取得資料
html_source = browser.page_source
soup = BeautifulSoup(html_source, "html5lib")

for d in soup.find(class_="part_list_2").find_all('h3'):
    if date_time in d.find(class_="date").text :
        break
    print(d.find(class_="date").text, d.find_all('a')[-1].text)

# 取得資料（整理成好的格式）
news = []

for d in soup.find(class_="part_list_2").find_all('h3'):
    if date_time in d.find(class_="date").text :
        break
    news.append({
        '時間': d.find(class_="date").text,
        '標題': d.find_all('a')[-1].text
    })

import pandas as pd
pd.DataFrame(news)

# 關閉瀏覽器

browser.close()

############################################################################################
# 2. 取出現在時間兩小時內的新聞

# 取得兩小時內的時間
from datetime import datetime, timedelta
two_hours_ago_time = datetime.now() - timedelta(hours=2)

# 取得資料（整理成好的格式）
news = []

for d in soup.find(class_="part_list_2").find_all('h3'):
    # 比兩小時前早的話就結束
    if datetime.strptime(d.find(class_="date").text, '%Y/%m/%d %H:%M') < two_hours_ago_time:
        break
    
    news.append({
        '時間': d.find(class_="date").text,
        '標題': d.find_all('a')[-1].text
    })

import pandas as pd
pd.DataFrame(news)

##############################################################################################

# 3. 根據範例，取出三天前下午三點到五點的新聞

from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome(executable_path='chromedriver')

browser.get("https://www.ettoday.net/news/news-list.htm")

# 取得三天前下午三點到五點的時間
from datetime import datetime, timedelta

date_time = datetime.now() - timedelta(3)
print("取得三天前時間：", date_time)

date_time_month = date_time.strftime("%m")
date_time_day = date_time.strftime("%d")
print("取得三天前時間（月）：", date_time_month)
print("取得三天前時間（日）：", date_time_day)


three_days_15_clock = datetime.strptime(date_time.strftime("%Y/%m/%d") + ' 15', '%Y/%m/%d %H')
three_days_17_clock = datetime.strptime(date_time.strftime("%Y/%m/%d") + ' 17', '%Y/%m/%d %H')
print("取得三天前下午三點：", three_days_15_clock)
print("取得三天前下午五點：", three_days_17_clock)

# 選擇且點選日期
from selenium.webdriver.support.ui import Select

selM = Select(browser.find_element_by_id("selM"))
selM.select_by_value(str(int(date_time_month)))
selD = Select(browser.find_element_by_id("selD"))
selD.select_by_value(str(int(date_time_day)))
browser.find_element_by_id('button').click()

# 利用 selenium 持續執行下滑的動作，直到取得要求時間內的新聞，表示取得完畢
import time
while True:
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "html5lib")
    new_date = soup.find_all(class_="part_list_2")[-1].find_all('h3')[-1].find(class_="date").text
    print(new_date)
    if datetime.strptime(new_date, '%Y/%m/%d %H:%M') < three_days_15_clock:
        print('==== STOP ====')
        break

# 取得資料（整理成好的格式）
news = []

for d in soup.find(class_="part_list_2").find_all('h3'):
    # 比兩小時前早的話就結束
    if datetime.strptime(d.find(class_="date").text, '%Y/%m/%d %H:%M') < three_days_15_clock:
        print('==== STOP ====')
        break
    
    if datetime.strptime(d.find(class_="date").text, '%Y/%m/%d %H:%M') < three_days_17_clock:
        news.append({
            '時間': d.find(class_="date").text,
            '標題': d.find_all('a')[-1].text
        })

import pandas as pd
pd.DataFrame(news2)

# 關閉瀏覽器

browser.close()
