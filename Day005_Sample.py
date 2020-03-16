# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020
API 資料串接 - 以 Dcard API 實作範例
了解 Dcard API 使用方式與回傳內容
撰寫程式存取 API 且解析 JSON 格式資料
@author: chenlw
"""

import requests
r = requests.get('https://www.dcard.tw/_api/forums/mood/posts?popular=true')
response = r.text

import json
data = json.loads(response)
count=1
for d in data:
    print('count=%d  ' %count,end="")
    print(d['title'])
    count+=1

print(data[0].keys())

# count=1
# for d in data:
#     print('count=%d  ' %count,end="")
#     print(d['title'],d['createdAt'],d['commentCount'],d['likeCount'])
#     count+=1

count=0
like_count=0
comm_count=0
for d in data:
    # print('count=%d,like_count=%d,comm_count=%d ' %(count,like_count,comm_count),end="")
    print(d['title'],d['commentCount'],d['likeCount'])
    count+=1
    like_count+=d.get('likeCount')
    comm_count+=d.get('commentCount')
    print('count=%d,like_count=%d,comm_count=%d ' %(count,like_count,comm_count))
print("熱門平均按讚次數%3.1f，熱門評論平均次數%3.1f\n\n" %(((like_count/(count)),(comm_count)/(count))))


r2 = requests.get('https://www.dcard.tw/_api/forums/mood/posts?popular=false')
response2 = r.text
data2 = json.loads(response)

count2=0
like_count2=0
comm_count2=0
for d1 in data2:
    # print('count=%d,like_count=%d,comm_count=%d ' %(count,like_count,comm_count),end="")
    print(d1['title'],d1['commentCount'],d1['likeCount'])
    count2+=1
    like_count2+=d.get('likeCount')
    comm_count2+=d.get('commentCount')
    print('count=%d,like_count=%d,comm_count=%d ' %(count2,like_count2,comm_count2))
print("非熱門平均按讚次數%3.1f，非熱門評論平均次數%3.1f" %(((like_count2/(count2)),(comm_count2)/(count2))))