# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:48:40 2020

@author: chenlw
"""

# 讀檔案
fh = open("./data/day003/64_72hr_CH.xml", "r",encoding="utf-8")
xml = fh.read()
fh.close()

# 解析檔案內容
import xmltodict
d = dict(xmltodict.parse(xml))


# 取出 datasetDescription
# datasetDescription = d['cwbopendata']['dataset']['datasetInfo']['datasetDescription']
datasetLocation = d['cwbopendata']['dataset']['locations']['location']
# print([datasetLocation])
area_len = len(datasetLocation)
print('高雄市有%d個地區有溫度資料' %area_len)

# # 請取出每一個地區所記錄的第一個時間點跟溫度
# try:
    
#     count =1
#     for No1 in range(len(datasetLocation)):
        
                
#         print('count',count)
#         print(datasetLocation[No1]['locationName'])
#         print(datasetLocation[No1]['weatherElement'][0]['time'][0]['dataTime'])
#         print(datasetLocation[No1]['weatherElement'][0]['time'][0]["elementValue"]["value"],"\n\n")
#         count +=1
# except:
#     print('something error!!')



#請取出第一個地區所記錄的每一個時間點跟溫度
try:
    
    count =1   
    for No3 in range(len(datasetLocation[0]['weatherElement'][0]['time'])):
    
        print('count',count)
        print(datasetLocation[0]['locationName'])
        print(datasetLocation[0]['weatherElement'][0]['time'][No3]['dataTime'])
        print(datasetLocation[0]['weatherElement'][0]['time'][No3]["elementValue"]["value"],"\n\n")
        count +=1
except:
    print('something error!!')



# count =1   
# for No3 in range(len(datasetLocation[0]['weatherElement'][0]['time'])):
    
#     print('count',count)
#     print(datasetLocation[0]['locationName'])
#     print(datasetLocation[0]['weatherElement'][0]['time'][No3]['dataTime'])
#     print(datasetLocation[0]['weatherElement'][0]['time'][No3]["elementValue"]["value"],"\n\n")
#     count +=1