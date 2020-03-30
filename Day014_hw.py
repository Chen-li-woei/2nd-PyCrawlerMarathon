# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""
import requests
import re
from bs4 import BeautifulSoup

# 先搜尋全部的電影代號(ID)資訊

# 查看目前上映那些電影，並擷取出其ID資訊
url = 'https://movies.yahoo.com.tw/'
resp = requests.get(url)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'lxml')
html = soup.find("select", attrs={'name':'movie_id'})
movie_item = html.find_all("option", attrs={'data-name':re.compile('.*')})

for p in movie_item:
    print("Movie: %s, ID: %s" % (p["data-name"], p["value"]))
 
    
    
    
# 參考前一個步驟中擷取到的ID資訊，並指定ID
movie_id = 10562




url = 'https://movies.yahoo.com.tw/api/v1/areas_by_movie_theater'
payload = {'movie_id':str(movie_id)}

# 模擬一個header
headers = {
    'authority': 'movies.yahoo.com.tw',
    'method': 'GET',
    'path': '/api/v1/areas_by_movie_theater?movie_id=' + str(movie_id),
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'cookie': 'rxx=9s3x2fws06.1g16irnc&v=1; _ga=GA1.3.2056742944.1551651301; GUC=AQEBAQFczFpdm0IfmwSB&s=AQAAACoo4N5D&g=XMsVBw; BX=4hkdk1decm57t&b=3&s=mr; _ga=GA1.4.2056742944.1551651301; nexagesuid=82843256dd234e8e91aa73f2062f8218; browsed_movie=eyJpdiI6IlJXWWtiSWJaZlNGK2MxQnhscnVUYWc9PSIsInZhbHVlIjoiMXRhMmVHRXRIeUNjc1RBWDJzdGYwbnlIQURmWGsrcjJSMzhkbkcraDNJVUNIZEZsbzU3amlFcVZ1NzlmazJrTGpoMjVrbHk1YmpoRENXaHZTOUw1TmI2ZTZVWHdOejZQZm16RmVuMWlHTTJLaTZLVFZZVkFOMDlTd1wvSGltcytJIiwibWFjIjoiZWQ2ZjA4MmVjZmZlYjlmNjJmYmY2NGMyMDI0Njc0NWViYjVkOWE2NDg0N2RhODMxZjBjZDhiMmJhZTc2MDZhYiJ9; avi=eyJpdiI6Im1NeWFJRlVRWDR1endEcGRGUGJUbVE9PSIsInZhbHVlIjoickRpU3JuUytmcGl6cjF5OW0rNU9iZz09IiwibWFjIjoiY2VmY2NkNzZmM2NhNjY5YzlkOTcyNjE5OGEyMzU0NWYxOTdmMDRkMDY3OWNmMmZjOTMxYjc5MjI5N2Q5NGE5MiJ9; cmp=t=1559391030&j=0; _gid=GA1.4.779543841.1559391031; XSRF-TOKEN=eyJpdiI6IkhpS2hGcDRQaHlmWUJmaHdSS2Q2bHc9PSIsInZhbHVlIjoiOUVoNFk4OHI1UUZmUWRtYXhza0MyWjJSTlhlZ3RnT0VGeVJPN2JuczVRMGRFdWt2OUlsamVKeHRobFwvcHBGM0dhU3VyMXNGTHlsb2dVM2l0U1hpUGxBPT0iLCJtYWMiOiJkZWU4YzJhNjAxMTY3MzE4Y2ExNWIxYmE1ZjE1YWZlZTlhOTcyYjc4M2RlZGY4ZWNjZDYyMTA2NGYwZGViMzc2In0%3D; m_s=eyJpdiI6InpsZHZ2Tk1BZ0dxaHhETml1RjBnUXc9PSIsInZhbHVlIjoiSkNGeHUranRoXC85bDFiaDhySTJqNkJRcWdjWUxjeVRJSHVYZ1wvd2d4bWJZUTUrSHVDM0lUcW5KNHdETFZ4T1lieU81OUhzc1VoUXhZcWk0UDZSQXVFdz09IiwibWFjIjoiYmJkMDJkMDhlODIzMzcyMWY4M2NmYWNjNGVlOWRjMDIwZmVmNzAyMjE3Yzg3ZGY3ODBkZWEzZTI4MTI5ZWNmOSJ9; _gat=1; nexagesd=10',
    'dnt': '1',
    'mv-authorization': '21835b082e15b91a69b3851eec7b31b82ce82afb',
    'referer': 'https://movies.yahoo.com.tw/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
    
resp = requests.get(url, params=payload, headers=headers)
#print(resp.json())  # 若有需要，列印出json原始碼

# 這裡回傳的格式是JSON格式的資料，要解析JSON擷取資料
for p in resp.json():
    print('放映地區: {0}, 代號(area_id): {1}'.format(p['title'], p['area_id']))




# 指定你想要觀看的放映地區，查詢有上映電影的場次日期
# 指定放映地區
area_id = 28
# 向網站發送請求
url = 'https://movies.yahoo.com.tw/movietime_result.html'
payload = {'movie_id':str(movie_id), 'area_id':str(area_id)}
resp = requests.get(url, params=payload)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'lxml')
movie_date = soup.find_all("label", attrs={'for':re.compile("date_[\d]")})

# 列印播放日期
for date in movie_date:
    print("%s %s" % (date.p.string, date.h3.string))





# 最後指定觀看的日期，查詢並列印出放映的電影院、放映類型(數位、3D、IMAX 3D...)、放映時間等資訊。
# 選定要觀看的日期
date = "2020-03-31"


# 向網站發送請求，獲取上映的電影院及時間資訊
url = "https://movies.yahoo.com.tw/ajax/pc/get_schedule_by_movie"
payload = {'movie_id':str(movie_id),
           'date':date,
           'area_id':str(area_id),
           'theater_id':'',
           'datetime':'',
           'movie_type_id':''}

resp = requests.get(url, params=payload)
# print(resp.json()['view'])  # 若有需要，列印出json原始碼

soup = BeautifulSoup(resp.json()['view'], 'lxml')
htmls = soup.find_all("ul", attrs={'data-theater_name':re.compile(".*")})

for html in htmls:
    # print("電影院名稱：%s \n影片放映類型：%s\n時間表：%s\n\n" % (html.a.string, html.span.string, html.label.string))

    # 電影院名稱：
    theater_name = html.find("li", attrs={"class":"adds"})
    print("電影院名稱：", theater_name.a.string)
    
    # 影片放映類型：
    tap_name = html.find("li", attrs={"class":"taps"})
    print("影片放映類型：", tap_name.span.string)
    
    # 時間表：
    theater_time = html.find_all("div", attrs={"class":"input_picker jq_input_picker"})
    print("時間表：", theater_time[0].text)
