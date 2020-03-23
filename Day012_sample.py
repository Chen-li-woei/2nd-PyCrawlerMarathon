# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")
a=[]
data = pd.DataFrame()
# 取出今天所有的發文
for d in soup.find(class_="part_list_2").find_all('h3'):
    print(d.find(class_="date").text,d.find("em").text, d.find_all('a')[-1].text)
    print(d.find(class_="date").text,d.find("em")['class'][1], d.find_all('a')[-1].text)
    a.append(d.find("em"))
    b ={'date':d.find(class_="date").text,'class':d.find("em")['class'][1], 'news':d.find_all('a')[-1].text}
    data = data.append(b,ignore_index=True)
    # a.append(d.find(class_="date").text,d.find("em")['class'][1], d.find_all('a')[-1].text)


# 如果想要依照類別分類，怎麼儲存會比較好？
result = data.sort_values(by=['class','date'],ascending=[0,1])
print(result)

# 哪一個類別的文章最多
result1 = result['class'].value_counts()
result1.head(1)
   

print("\n\n最多的前三種新聞為\n%s" %result1.head(3))