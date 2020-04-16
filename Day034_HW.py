# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:38:09 2020

@author: chenlw
"""

import requests
from bs4 import BeautifulSoup
import random

proxy_ips = []
res = requests.get('https://free-proxy-list.net/')
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.text)

# html = browser.page_source
soup = BeautifulSoup(res.text, 'lxml')
ip_list = soup.find("tbody").find_all('td')

for a in range(30):
    b = ip_list[0+a*8].text + ":" + ip_list[1+a*8].text
    proxy_ips.append(b)
print(proxy_ips)

for i in range(10):
    ip = random.choice(proxy_ips)
    print('Use', ip)
    try:
        resp = requests.get('http://ip.filefab.com/index.php',
                        proxies={'http': ip, 'https': ip}, timeout=10)
        soup = BeautifulSoup(resp.text, 'html5lib')
        print(soup.find('h1', id='ipd').text.strip())
    except:
        print('Fail')

############################################解答


from bs4 import BeautifulSoup
import requests
import random

proxy_ips = []

# 對 https://free-proxy-list.net/ 發送請求，並從表格中整理出免費的代理伺服器

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
url = 'https://free-proxy-list.net/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

for tr in soup.find('tbody').find_all('tr')[:100]:
    proxy = tr.find_all('td')[0].text + ':' + tr.find_all('td')[1].text
    proxy_ips.append(proxy)
    
print(proxy_ips)

# 將免費的代理伺服器，發送至 http://ip.filefab.com/index.php 找出可用的代理伺服器

available_proxies = []

for i in range(100):
    ip = proxy_ips[i]
    print('Use', ip)
    try:
        resp = requests.get('http://ip.filefab.com/index.php',
                        proxies={'http': ip, 'https': ip}, timeout=10)
        soup = BeautifulSoup(resp.text, 'html5lib')
        print(soup.find('h1', id='ipd').text.strip())
        available_proxies.append(ip)
        if len(available_proxies) > 5:
            break
    except:
        print('Fail')
    
print(available_proxies)







