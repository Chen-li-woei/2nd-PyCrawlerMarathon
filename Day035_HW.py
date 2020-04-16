# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:38:09 2020

@author: chenlw
"""

import requests
from bs4 import BeautifulSoup
import time
import _thread

board = ['stock', 'baseball', 'nba', 'car', 'playstation']
################################### 單線程 ###############################
startTime1 = time.time()
for a in board:
    url = 'https://www.ptt.cc/bbs/'+a
    r = requests.get(url, cookies={'over18': '1'})
    
    soup = BeautifulSoup(r.text, "html5lib")
    
    for d in soup.find_all(class_="title"):
        print(d.text.replace('\t', '').replace('\n', ''))
        try:
            r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
            print('https://www.ptt.cc'+d.find('a')['href'])
            print('作者: ' + r.find_all(class_='article-meta-value')[0].text+ r.find_all(class_='article-meta-value')[3].text)
        except:
            continue
finishTime1 = time.time()
print(finishTime1 - startTime1)
print('\n\n\n\n\n')
###############################  多線程 ##########################

def web_get(url):
    
    r = requests.get(url, cookies={'over18': '1'})
    
    soup = BeautifulSoup(r.text, "html5lib")
    
    for d in soup.find_all(class_="title"):
        print(d.text.replace('\t', '').replace('\n', ''))
        try:
            r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
            print('https://www.ptt.cc'+d.find('a')['href'])
            print('作者: ' + r.find_all(class_='article-meta-value')[0].text+ r.find_all(class_='article-meta-value')[3].text)
        except:
            continue

startTime2 = time.time()
for b in board:
    url = 'https://www.ptt.cc/bbs/'+b
    try:
        _thread.start_new_thread(web_get, (url, ))
        
    except:
        print('Fail')
    
finishTime2 = time.time()
print(finishTime2 - startTime2)

