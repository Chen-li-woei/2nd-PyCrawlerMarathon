# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Wikipedia爬蟲練習

@author: chenlw
"""

import requests
url = 'http://aicoin.cn/'

headers = {
#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#'Accept-Encoding': 'gzip, deflate, br',
#'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
#'Cache-Control': 'max-age=0',
#'Connection': 'keep-alive',
#'Cookie': 'HWWAFSESID=e529373557371c1925; HWWAFSESTIME=1585733489048; _pk_testcookie..undefined=1; _pk_testcookie.2.57ea=1; _pk_ref.2.57ea=%5B%22%22%2C%22%22%2C1585733493%2C%22http%3A%2F%2Flocalhost%3A8888%2Fnotebooks%2FDay018_HW.ipynb%22%5D; _pk_id.2.57ea=d104e020d1efcbb3.1585733493.1.1585733493.1585733493.; _pk_ses.2.57ea=1; _ga=GA1.2.342222719.1585733493; _gid=GA1.2.2134580654.1585733493; _gat_gtag_UA_108140256_2=1; Hm_lvt_3c606e4c5bc6e9ff490f59ae4106beb4=1585733493; Hm_lpvt_3c606e4c5bc6e9ff490f59ae4106beb4=1585733493; aicoin_session=eyJpdiI6IlQ1T1pYaHlxOWJ6RmFTdkt1akU4Q0E9PSIsInZhbHVlIjoiK3lpbnI3MHhySHAzVFlSc2s3YU8xWDJNQXpzYVwvYkhMeEVXYThGT1ZPYnphVDNxalI1SG5CZGVkdmVsQzc5WmFkdHEyWWtYS2hZc0o4VEdOOWtWQUJBPT0iLCJtYWMiOiI4YWU4NzkyY2FkNzYyY2ViODA2Y2I1ZmU0ZjJhMGFjZmU0YzNhNWNjYmZkYTFjMGNjYTQ3M2IwZDk2MDc5ZTRjIn0%3D',
# 'Host': 'www.aicoin.cn',
# 'If-None-Match': 'W/"12870d-n/i8WSfVY3JGOpBG7FDkcHVICIU"',
# 'Referer': 'http://localhost:8888/notebooks/Day018_HW.ipynb',
# 'Sec-Fetch-Dest': 'document',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-Site': 'same-origin',
# 'Sec-Fetch-User': '?1',
# 'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

r = requests.get(url, headers=headers)
print(r.text[0:600])