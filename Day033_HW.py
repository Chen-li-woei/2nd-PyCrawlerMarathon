# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:38:09 2020

@author: chenlw
"""

import requests
from bs4 import BeautifulSoup

############################################################################################
#----------------------範例  被擋-------------------------------------

res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify = False)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.text)

#--------------------模仿授權機制 方法一：先送登入，再送請求-------------------

# rs = requests.session()
# payload={
#     'from':'/bbs/Gossiping/index.html',
#     'yes': 'yes'
# }
# res = rs.post('https://www.ptt.cc/ask/over18',verify = False, data = payload)
# res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',verify = False)
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup.text) 

#--------------------模仿授權機制 方法二：在請求中帶入 cookie----------------

# res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html',verify = False, cookies={'over18': '1'})
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup.text)


###########///////////////////////////////////////////////////////////////////////////////////
#################################作業   被擋  ################################################

# res = requests.get('https://www.eyny.com/forum-336-1.html', verify = False)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.text)

#################################成功

rs = requests.session()
payload={
    'agree': 'yes'
}
res = rs.post('https://www.eyny.com/forum-336-1.html',verify = False, data = payload)
res = rs.get('https://www.eyny.com/forum-336-1.html',verify = False)
soup = BeautifulSoup(res.text,'html.parser')
print(soup.text) 












