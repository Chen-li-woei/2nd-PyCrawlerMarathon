# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

空氣污染監測網 網路爬蟲實作練習
能夠利用 selenium + BeautifulSoup 撰寫動態爬蟲
空氣污染監測網 網頁爬蟲
如果利用原本的 Request 的方式，會發現怎麼拉都是空資料。原因在於資料一樣是透過 JavaScript 動態載入的。

@author: chenlw
"""

# 打開瀏覽器

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome(executable_path='chromedriver')

browser.get("http://taqm.epa.gov.tw/taqm/tw/MonthlyAverage.aspx")

time.sleep(1)
# 模擬使用者操作行為，選擇/點擊

selectSite = Select(browser.find_element_by_id("ctl05_ddlSite"))
selectSite.select_by_value('29')
selectYear = Select(browser.find_element_by_id("ctl05_ddlYear"))
selectYear.select_by_value('2014')

browser.find_element_by_id('ctl05_btnQuery').click()
time.sleep(1)
# 取得資料，丟到 BeautifulSoup 解析

html_source = browser.page_source

soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find('table', class_='TABLE_G')
print(table)

# 關閉瀏覽器
browser.quit();








