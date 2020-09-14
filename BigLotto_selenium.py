# 大樂透開獎(selenium)
import requests
url="http://www.taiwanlottery.com.tw/"
from bs4 import BeautifulSoup
from selenium import webdriver
browser=webdriver.Chrome()
browser.get(url)

html=requests.get(url).text
sp=BeautifulSoup(html,"html.parser")

rightdown=sp.select("#rightdown")[0]
#print(rightdown)
    
# 大樂透在 contents_box02[2]
biglotto=rightdown.find_all("div",{"class":"contents_box02"})[2]
#print(biglotto) 
#第幾期
no=biglotto.find("span",{"class":"font_black15"}).text

# 大樂透號，共 12 個 
ball_yellow=biglotto.find_all("div",{"class":"ball_tx ball_yellow"})

#紅球 1 個 
ball_red=biglotto.find("div",{"class":"ball_red"})

print("大樂透第 {} 開獎結果" .format(no))
print("開出順序:",end=" ")
for i in range(0,6):
    print(ball_yellow[i].text,end=" ")

print("\n大小順序:",end=" ")
for i in range(6,12):
    print(ball_yellow[i].text,end=" ")
    
print("\n特 別 號:",end=" ")
for i in range(21,22):
    print(ball_red.text,end=" ")    
    
#print("\n紅    球:",ball_red.text)    


browser.quit()