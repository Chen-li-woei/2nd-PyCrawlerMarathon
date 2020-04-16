# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""
####印出最新文章的「作者」「標題」「時間」
# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.ptt.cc/bbs/NBA/index.html'
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html5lib")

# for d in soup.find_all(class_="title"):
#     print(d.text.replace('\t', '').replace('\n', ''))
#     try:
#         r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
#         print('作者: ' + r.find_all(class_='article-meta-value')[0].text+ r.find_all(class_='article-meta-value')[3].text)
#     except:
#         continue





####印出第一頁文章的「作者」「標題」「時間」
# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.ptt.cc/bbs/NBA/index1.html'
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html5lib")

# for d in soup.find_all(class_="title"):
#     print(d.text.replace('\t', '').replace('\n', ''))
#     try:
#         r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
#         print('作者: ' + r.find_all(class_='article-meta-value')[0].text+ r.find_all(class_='article-meta-value')[3].text)
#     except:
#         continue



#########試著爬爬看其他版的文章

# import requests
# from bs4 import BeautifulSoup
# ##NBA可以抓
# url = 'https://www.ptt.cc/bbs/NBA/index.html'
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html5lib")

# for d in soup.find_all(class_="title"):
#     print(d.text.replace('\t', '').replace('\n', ''))
#     try:
#         r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
#         print('https://www.ptt.cc'+d.find('a')['href'])
#         print('作者: ' + r.find_all(class_='article-meta-value')[0].text+ r.find_all(class_='article-meta-value')[3].text)
#     except:
#         continue



import requests
from bs4 import BeautifulSoup
## beauty、sex、政治不能抓

url = 'https://www.ptt.cc/bbs/nba/index.html'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

for d in soup.find_all(class_="title"):
    print(d.text.replace('\t', '').replace('\n', ''))
    try:
        r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
        print('https://www.ptt.cc'+d.find('a')['href'])
        print('作者: ' + r.find_all(class_='article-meta-value')[0].text+ r.find_all(class_='article-meta-value')[3].text)
    except:
        continue
