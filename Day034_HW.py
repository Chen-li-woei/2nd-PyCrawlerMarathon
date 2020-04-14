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









