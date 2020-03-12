# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:55:01 2020

@author: chenlw
"""

import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='',encoding='utf-8-sig') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row[5])