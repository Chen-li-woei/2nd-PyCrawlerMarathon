# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

@author: chenlw
"""

import re  #載入re模組
# 定義一個函數，用來測試是否能匹配正規表達式
def RegexMatchingTest(regex, input_text):
    #將正規表達式轉換成pattern
    pattern = re.compile(regex)
    
    # 使轉換後的pattern，來測試是否匹配
    result = re.search(pattern, input_text)

    if result:
        # 匹配完的結果會儲存在group()的屬性中，我們可以把匹配的結果列印出來
        # print("IP: %s" % (result.group()))
        
        if result.lastindex is not None:
            # group(0)代表整個字串，group(1)、group(2)...代表分組中，匹配的內容
            # print(result.lastindex,type(result.lastindex))
            if result.lastindex == 4:
                print("\nIP: %s" % (result.group()))
                for i in range(1, result.lastindex+1):
                    a=int(result.group(i))
                    # print("  group(%d): %s" % (i, result.group(i)),type(result.group(i)))
                    if a<0 or a>255:
                        print(a,"IP範圍錯誤")
                    else:
                        print("  group(%d): %d" % (i, a),type(a))
                
            else:
                for i in range(0, result.lastindex+1):
                    print("\ngroup(%d): %s" % (i, result.group(i)),type(result.group(i)))
                
    else:
        print("Not matched.")

test_string = "Google IP address is 216.58.200.227"

# 過濾IP address的regex pattern
regex = '(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})'
RegexMatchingTest(regex, test_string)

'''
    Your code here.
    hint: 把IP可能出現的數字範圍，分開來思考
          1. 000 ~ 199
          2. 200 ~ 249
          3. 250 ~ 255
'''
# regex = 

test_string1 = "Test IP 216.58.200.227"
RegexMatchingTest(regex, test_string1)  #測試表達式是否會匹配此合法IP

test_string2 = "Test IP 999.888.777.666"
RegexMatchingTest(regex, test_string2)  #測試表達式是否會匹配此不合法IP

html_a_tag = "<a href=https://movies.yahoo.com.tw/movietime_result.html/id=9467> 時刻表 </a>"

# '''
#     Your code here.
#     過濾URL的regex pattern
# '''
regex = 'href=(\S+)>'
RegexMatchingTest(regex, html_a_tag)