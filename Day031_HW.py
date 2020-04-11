# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:38:09 2020

@author: chenlw
"""


# import requests
# headers = {'user-agent': '1'}

# r = requests.get('https://www.zhihu.com/',headers=headers)
# r.encoding = 'utf-8'
# response = r.text



# headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

# r2 = requests.get('https://www.zhihu.com/',headers=headers2)
# r2.encoding = 'utf-8'
# response2 = r2.text


import requests
# headers = {'user-agent': '1'}
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

r = requests.get('https://blog.csdn.net/')
r.encoding = 'utf-8'
response = r.text
