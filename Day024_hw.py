# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

從104人力銀行網站爬取求職公司資訊。

@author: chenlw
"""

# import pandas as pd
# import re, time, requests
# from selenium import webdriver
# from bs4 import BeautifulSoup

# # 加入使用者資訊(如使用什麼瀏覽器、作業系統...等資訊)模擬真實瀏覽網頁的情況
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

# # 查詢的關鍵字
# my_params = {'ro':'1', # 限定全職的工作，如果不限定則輸入0
#              'keyword':'資料科學', # 想要查詢的關鍵字
#              'area':'6001001000', # 限定在台北的工作
#              'isnew':'30', # 只要最近一個月有更新的過的職缺
#              'mode':'l'} # 清單的瀏覽模式

# url = requests.get('https://www.104.com.tw/jobs/search/?' , my_params, headers = headers).url
# driver = webdriver.Chrome()
# driver.get(url)


#######################################################################################
import time
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# 開啟新網頁後，觀察新的網址內容，把網址複製下來。
job_104_url = "https://www.104.com.tw/cust/list/index/?page=1&order=1&mode=s&jobsource=checkc&area=6001001000&indcat=1001002000"







opts = webdriver.ChromeOptions()
# opts.add_argument("--incognito")  # 使用無痕模式。用 selenium開瀏覽器已經很乾淨了，但疑心病重的可以用一下
# proxy = "socks5://localhost:9050"
# opts.add_argument('--proxy-server={}'.format(proxy))  # 讓 selenium透過 tor訪問 internet
# ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
# opts.add_argument("user-agent={}".format(ua))         # 使用偽造的 user-agent
# driver = webdriver.Chrome(executable_path='/path/to/your/chromedriver',chrome_options=opts)

prefs = {
        # "profile.managed_default_content_settings.images":1,
        # "profile.content_settings.plugin_whitelist.adobe-flash-player":1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1,
    }
opts.add_experimental_option('prefs',prefs)



# 開始爬取搜尋結果
browser = webdriver.Chrome(chrome_options=opts)

# browser.get('http://httpbin.org/user-agent')



browser.get(job_104_url)  # 打開瀏覽器並連到網頁
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
    if (soup.find("a", attrs={'class':'page-next disabled'})):
        break
    else:
        browser.find_element_by_link_text(u"下一頁").click()
        

browser.quit()    


#company-pages > div > div.page-ctrl > a.page-next.disabled

#//*[@id="company-pages"]/div/div[1]/a[10]

# soup.find("a", attrs={'class':'page-next disabled'})


