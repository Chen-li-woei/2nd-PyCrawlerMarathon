# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020
利用 Python 存取 API
了解 Server Client 的架構與溝通方法
知道 HTTP Request & Response 的內容
什麼是 API？如何用 Python 程式存取 API 資料
@author: chenlw
"""

# import requests

# r = requests.get('https://api.github.com/events')
# r.text


# import json

# json.loads(r.text)


# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# json.loads(r.text)


# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# json.loads(r.text)


# 自行尋找一個合適的 API 接口做練習，並且查看其回傳內容
# https://cat-fact.herokuapp.com/facts (來源：https://alexwohlbruck.github.io/cat-facts/)
# http://odata.wra.gov.tw/v4/RealtimeWaterLevel (來源：https://data.gov.tw/dataset/25768)


import requests

r = requests.get('https://cat-fact.herokuapp.com/facts')
a=r.text

data1=open(".\hw04_r_text.txt",'w+', encoding="utf-8") 
print('r.text=\n',a,file=data1)
data1.close()


import json
data2=open(".\hw04_json.txt",'w+', encoding="utf-8") 
print('json.loads(r.text)=\n',json.loads(a),file=data2)
data2.close()
