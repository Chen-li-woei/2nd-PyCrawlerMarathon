# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

從104人力銀行網站爬取求職公司資訊。

@author: chenlw
"""

import pandas as pd
import re, time, requests
from selenium import webdriver
from bs4 import BeautifulSoup

# 加入使用者資訊(如使用什麼瀏覽器、作業系統...等資訊)模擬真實瀏覽網頁的情況
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

# 查詢的關鍵字
my_params = {'ro':'1', # 限定全職的工作，如果不限定則輸入0
             'keyword':'電信及通訊相關業', # 想要查詢的關鍵字
             'area':'6001001000', # 限定在台北的工作
             'isnew':'30', # 只要最近一個月有更新的過的職缺
             'mode':'l'} # 清單的瀏覽模式

url = requests.get('https://www.104.com.tw/jobs/search/?' , my_params, headers = headers).url
browser = webdriver.Chrome()
browser.get(url)

time.sleep(2)  # delay一段時間等待網頁更新完成

while True:
    time.sleep(3)  # delay一段時間等待網頁更新完成
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    company_list = soup.find("div", attrs={'id':"company-result"}).find_all("article", attrs={'class':"items"})
    
    #
    # 擷取公司名稱及簡介內容
    #
    for company in company_list:
        # 因為內容太多，我們把爬取到的結果，寫入"company_list.txt"檔案中，稍後再來檢視
        company_name = company.a.string
        f = open("company_list.txt", "a+", encoding='utf-8')
        f.write( company_name + "\n" )  # 寫入公司名稱
        
        company_desc = company.find("p", attrs={'class':"desc"})
        f.write( company_desc.string + "\n" )  # 寫入公司簡介
        f.write( "--------------------------------------------------------------------------------" + "\n" )
        f.close()

    '''
    
    接下來請學員練習，定位到「下一頁」按鈕。(可以利用find_element_by_link_text("xxx")的函式)
    如果還有下一頁，利用Selenium模擬click「下一頁」按鈕的動作。(定位到物件後，利用其click()屬性)
    若沒有下一頁了，離開爬取的流程
    
    Your code here
    
    '''

browser.quit()    