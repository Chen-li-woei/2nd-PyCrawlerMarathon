# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:38:09 2020

@author: chenlw
"""


import requests
import pytesseract
from PIL import Image
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# response = requests.get('https://i0.wp.com/www.embhack.com/wp-content/uploads/2018/06/hello-world.png')
# img = Image.open(BytesIO(response.content))


img = Image.open("./data/test/test1.png")           #619121
# img = Image.open("./data/test/test2.png")

img1 = Image.open("./data/test/test2.png").convert("1")    #像素点变成黑白两种点，要么是0，要么是255。
img2 = Image.open("./data/test/test2.png").convert("L")    #像素值为[0,255]之间的某个数值。
img3 = Image.open("./data/test/test2.png").convert("P")    #像素值为[0,255]之间的某个数值，但它为调色板的索引值，其最终还是彩色图像。
img4 = Image.open("./data/test/test2.png").convert("RGBA") #图像从三通道变成了四通道，其R、G、B三个通道的数值没有变化，新增的alpha通道均为255，表示不透明。
img5 = Image.open("./data/test/test2.png").convert("RGB")  #原始 RGB圖像
img6 = Image.open("./data/test/test2.png").convert("YCbCr")  #YCbCr圖像
img7 = Image.open("./data/test/test2.png").convert("I")  #将三通道变成了单通道，I = R * 299/1000+ G * 587/1000 + B * 114/1000
img8 = Image.open("./data/test/test2.png").convert("F")  #将彩色图像变成了32位浮点灰色图像。F = R * 299/1000+ G * 587/1000 + B * 114/1000

print(img1.getpixel((0,0)))
img1
print(img2.getpixel((0,0)))
img2
print(img3.getpixel((0,0)))
img3
print(img4.getpixel((0,0)))
img4
print(img5.getpixel((0,0)))
img5
print(img6.getpixel((0,0)))
img6
print(img7.getpixel((0,0)))
img7
print(img8.getpixel((0,0)))
img8

code = pytesseract.image_to_string(img)

code1 = pytesseract.image_to_string(img1)
code2 = pytesseract.image_to_string(img2)
code3 = pytesseract.image_to_string(img3)
code4 = pytesseract.image_to_string(img4)
code5 = pytesseract.image_to_string(img5)
code6 = pytesseract.image_to_string(img6)
code7 = pytesseract.image_to_string(img7)
code8 = pytesseract.image_to_string(img8)

print("-----------------------------------------------")
print(code)
print()
print(code1)
print(code2)
print(code3)
print(code4)
print(code5)
print(code6)
print(code7)
print(code8)

#-----------------------------------解答-------------------------
def binarizing(img,threshold): #input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img

img9 = Image.open("./data/test/test2.png").convert("L")
img9 = binarizing(img9, 100)
img9 = depoint(img9)
img9
code9 = pytesseract.image_to_string(img9)
print(code9)