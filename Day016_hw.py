# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Wikipedia爬蟲練習

@author: chenlw
"""

# 範例：練習是從Wikipedia中爬取文章。先定義一個搜尋的關鍵字，擷取該關鍵字詞的文章。

import requests
import re
from bs4 import BeautifulSoup

# 先定義一個我們想搜尋的字詞，並將它轉換成UTF-8編碼後的URL

input_keyword = "網路爬蟲"  # 這裡可以自己定義有興趣的關鍵字

utf8_url = repr(input_keyword.encode('UTF-8')).upper()  # 編碼成UTF-8並轉成大寫字元
utf8_url = utf8_url.replace("\\X", "%")                 # 用 '%' 取代 '\X' 
print("%s: %s" % (input_keyword, utf8_url[2:-1:1]))     # 擷取中間的編碼結果

# 組成Wiki關鍵字搜尋的網址格式
root_keyword_link = '/wiki/' + utf8_url[2:-1:1]
print(root_keyword_link)

# 範例1：送出關鍵字請求後，爬取該關鍵字的文章內容

# 模擬封包的標頭
headers = {
    'authority': 'zh.wikipedia.org',
    'method': 'GET',
    'path': '/wiki/' + root_keyword_link,
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'cookie': 'GeoIP=TW:TPE:Taipei:25.05:121.53:v4; TBLkisOn=0; mwPhp7Seed=8b8; WMF-Last-Access-Global=04-Jun-2019; WMF-Last-Access=04-Jun-2019',
    'dnt': '1',
    #'if-modified-since': 'Tue, 04 Jun 2019 12:03:22 GMT',
    'referer': 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}    

url = 'https://zh.wikipedia.org' + root_keyword_link  # 組合關鍵字查詢URL
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

html = BeautifulSoup(resp.text, "lxml")
content = html.find(name='div', attrs={'id':'mw-content-text'}).find_all(name='p')

#
# 解析回傳資料，並萃取文章內容
#
for paragraph in content:
    print(paragraph.get_text())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 範例2：從爬取的文章內容中，擷取出有外部連結的關鍵字。這些關鍵字在文章中是以藍色字體顯示，會連到外部的網頁，並解釋其內容。
external_link_dict = dict({})
# external_link_list = []

for ext_link in content:
    a_tag = ext_link.find_all('a', href=re.compile("^(/wiki/)((?!;)\S)*$"))
    if len(a_tag) > 0:
        for link_string in a_tag:
            a_link = link_string["href"]       # 外部連結的網址
            a_keyword = link_string.get_text()  # 外部連結的中文名稱
            external_link_dict[a_link]=a_keyword
            print("外部連結: [%s] %s" % (a_keyword, a_link))
            


# 作業：接下來定義一個爬蟲函數，這個函數的主要工作為：
# (1) 爬取當前關鍵字的解釋，並存入檔案(因為文章內容太多會佔滿整個頁面，所以存程檔案，方便後續檢視)
# (2) 萃取出當前關鍵字所引用的外部連結，當作新的查詢關鍵字
# (3) 把第(2)擷取到的關鍵字當作新的關鍵字，回到第(1)步，爬取新的關鍵字解釋。

def WikiArticle(key_word_link, key_word, recursive):
    
    if (recursive <= max_recursive_depth):
        print("遞迴層[%d] - %s (%s)" % (recursive, key_word_link, key_word))
        
        # 模擬封包的標頭
        headers = {
            'authority': 'zh.wikipedia.org',
            'method': 'GET',
            'path': '/wiki/' + key_word_link,
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'cookie': 'GeoIP=TW:TPE:Taipei:25.05:121.53:v4; TBLkisOn=0; mwPhp7Seed=8b8; WMF-Last-Access-Global=04-Jun-2019; WMF-Last-Access=04-Jun-2019',
            'dnt': '1',
            #'if-modified-since': 'Tue, 04 Jun 2019 12:03:22 GMT',
            'referer': 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }    

        url = 'https://zh.wikipedia.org' + key_word_link  # 組合關鍵字查詢URL
        resp = requests.get(url, headers=headers)
        resp.encoding = 'utf-8'

        html = BeautifulSoup(resp.text, "lxml")
        content = html.find(name='div', attrs={'id':'mw-content-text'}).find_all(name='p')
        
        #
        # Part 1: 請參考範例1，爬取當前關鍵字的文章內容。
        #         因為內容太多，我們把它寫入檔案，並以關鍵字作為檔案名稱，以便稍後查閱內容。
        #         請先建立一個名為"WikiArticle"的資料夾，爬取到的文章內容會放在這個資料夾底下。
        #
        
        
        #
        # 解析回傳資料，並萃取文章內容
        #
        
        
        
        key_word1 = key_word.replace("/", "-")                 # 用 '%' 取代 '\X' 
        fn = './WikiArticle/' + key_word1 + '.txt'
        with open(fn, 'w', encoding="utf-8") as file_Obj:
            for paragraph in content:
                print(paragraph.get_text(),file=file_Obj)
        
        
        
        
        
        
        #
        # Part 2: 請參考範例2，萃取出本篇文章中所延伸引用的外部連結，並儲存在external_link_dict
        #
        # external_link_dict = dict({})
        
        # external_link_dict[key_word_link]=key_word
                
        for ext_link in content:
            a_tag = ext_link.find_all('a', href=re.compile("^(/wiki/)((?!;)\S)*$"))
            if len(a_tag) > 0:
                for link_string in a_tag:
                    a_link = link_string["href"]       # 外部連結的網址
                    a_keyword = link_string.get_text()  # 外部連結的中文名稱
                    # external_link_dict[a_link]=a_keyword
                    print("外部連結: [%s] %s" % (a_keyword, a_link))
        print("\n\n")
        
        '''
        
        Your code here
        
        '''
                   
        #
        # Part 3: 將Part 2所收集的外部連結，當作新的關鍵字，繼續迭代深入爬蟲
        #
        # recursive = 0
        if (len(external_link_dict) > 0):
            
            recursive = recursive + 1  # 遞迴深度加1
            
            for k, v in external_link_dict.items():
                
                
                WikiArticle(k, v, recursive)  # 再次呼叫同樣的函數，執行同樣的流程
                
                # del external_link_dict[k]
# 執行前個步驟定義好的爬蟲主程式

# 定義爬取的遞迴深度。深度不要訂太深，否則會爬很久。
                
# external_link_dict = dict({})

max_recursive_depth = 2

WikiArticle(root_keyword_link, input_keyword, 0)

