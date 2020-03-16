# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020
API 資料串接 - 以 知乎網站 API 實作範例
了解知乎 API 使用方式與回傳內容
撰寫程式存取 API 且添加標頭
@author: chenlw
"""
##### 直接用程式要求，會連線錯誤
# import requests
# r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers')
# response = r.text

# response

#需加上user-agent，或用正常網頁連線才行。
import requests
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers=headers)
response = r.text

response



import time
import json
data = json.loads(response)

####取出知乎問題發問時間

for d in data['data']:
    print(time.ctime(d['created_time']))

####取出第一筆與最後一筆回答的時間

print("第一筆回答時間：",time.ctime(data['data'][0]['updated_time']))
print("最後一筆回答時間：",time.ctime(data['data'][-1]['updated_time']))