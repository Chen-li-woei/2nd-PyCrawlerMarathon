# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""
import requests
import re
from bs4 import BeautifulSoup

# 先觀察一下目前上映中的電影數量
url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
resp = requests.get(url)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'lxml')
html = soup.find("div", attrs={'class':'release_box'})  # 尋找正在上映中的全部電影筆數，其所在的tag
print("正在上映中總共: ", html.p.string)

# 接下來要爬取每一頁的電影介紹
# 先點選網頁最底部的下一頁，觀察其網址變化。然後我們把頁數當作變數傳入，用迴圈爬取。
max_page = 5
for page_number in range(1, max_page+1, 1):
    url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
    payload = {'page':str(page_number)}
    resp = requests.get(url, params=payload)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')

    # 把電影介紹擷取出來
    movie_list = soup.find("ul", attrs={"class":"release_list"}).find_all("li")
    for p in movie_list:
        print("----------------------------------------------------------------------")
        # 電影名稱
        movie_name = p.find("div", attrs={"class":"release_movie_name"})
        print("電影名稱：", movie_name.a.string)
        
        # 定位電影評價資訊欄位
        level_box = movie_name.find("dl", attrs={"class":"levelbox"})
        
        # 期待度
        expectation = level_box.find("div", attrs={"class":"leveltext"})
        print("期待度：", expectation.span.string)
        
        # 滿意度
        satisfaction = level_box.find_all("div", attrs={"class":"leveltext"})
        print("滿意度：", satisfaction[1].span["data-num"])  # 滿意度可以從"data-num"這個屬性擷取
        # print("滿意度：", satisfaction[1].span.text)  # 滿意度可以從"data-num"這個屬性擷取
        
        # 簡介
        movie_info = p.find("div", attrs={"class":"release_text"})
        print(movie_info.span.string)


