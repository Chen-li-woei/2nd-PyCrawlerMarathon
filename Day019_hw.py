# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Wikipedia爬蟲練習

@author: chenlw
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd



browser = webdriver.Chrome(executable_path='chromedriver')
browser.get("http://taqm.epa.gov.tw/taqm/tw/MonthlyAverage.aspx")


################取得台中--沙鹿(29) 2014 #############################

# selectSite = Select(browser.find_element_by_id("ctl05_ddlSite"))
# selectSite.select_by_value('29')
# selectYear = Select(browser.find_element_by_id("ctl05_ddlYear"))
# selectYear.select_by_value('2014')



################取得高雄--小港(58) 2019 #############################

selectSite = Select(browser.find_element_by_id("ctl05_ddlSite"))
selectSite.select_by_value('58')
selectYear = Select(browser.find_element_by_id("ctl05_ddlYear"))
selectYear.select_by_value('2019')

browser.find_element_by_id('ctl05_btnQuery').click()

# 取得資料（等瀏覽器資料出現後才執行）
sleep(1)

html_source = browser.page_source
html_source

soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find('table', class_='TABLE_G')
print(table)

d = pd.read_html(html_source)
# df = pd.DataFrame(table)
browser.close()               #關閉瀏覽器


'''
測站資料

<option selected="selected" value="11">臺北市-士林</option>
		<option value="16">臺北市-大同</option>
		<option value="12">臺北市-中山</option>
		<option value="14">臺北市-古亭</option>
		<option value="15">臺北市-松山</option>
		<option value="64">臺北市-陽明</option>
		<option value="13">臺北市-萬華</option>
		<option value="51">高雄市-大寮</option>
		<option value="58">高雄市-小港</option>
		<option value="49">高雄市-仁武</option>
		<option value="54">高雄市-左營</option>
		<option value="52">高雄市-林園</option>
		<option value="56">高雄市-前金</option>
		<option value="57">高雄市-前鎮</option>
		<option value="47">高雄市-美濃</option>
		<option value="71">高雄市-復興</option>
		<option value="53">高雄市-楠梓</option>
		<option value="50">高雄市-鳳山</option>
		<option value="48">高雄市-橋頭</option>
		<option value="1">基隆市-基隆</option>
		<option value="24">新竹市-新竹</option>
		<option value="30">臺中市-大里</option>
		<option value="32">臺中市-西屯</option>
		<option value="29">臺中市-沙鹿</option>
		<option value="31">臺中市-忠明</option>
		<option value="28">臺中市-豐原</option>
		<option value="42">嘉義市-嘉義</option>
		<option value="45">臺南市-安南</option>
		<option value="44">臺南市-善化</option>
		<option value="43">臺南市-新營</option>
		<option value="46">臺南市-臺南</option>
		<option value="67">新北市-三重</option>
		<option value="5">新北市-土城</option>
		<option value="70">新北市-永和</option>
		<option value="2">新北市-汐止</option>
		<option value="9">新北市-林口</option>
		<option value="6">新北市-板橋</option>
		<option value="10">新北市-淡水</option>
		<option value="84">新北市-富貴角</option>
		<option value="8">新北市-菜寮</option>
		<option value="4">新北市-新店</option>
		<option value="7">新北市-新莊</option>
		<option value="3">新北市-萬里</option>
		<option value="66">宜蘭縣-冬山</option>
		<option value="65">宜蘭縣-宜蘭</option>
		<option value="18">桃園市-大園</option>
		<option value="68">桃園市-中壢</option>
		<option value="20">桃園市-平鎮</option>
		<option value="17">桃園市-桃園</option>
		<option value="21">桃園市-龍潭</option>
		<option value="19">桃園市-觀音</option>
		<option value="23">新竹縣-竹東</option>
		<option value="22">新竹縣-湖口</option>
		<option value="27">苗栗縣-三義</option>
		<option value="26">苗栗縣-苗栗</option>
		<option value="25">苗栗縣-頭份</option>
		<option value="35">彰化縣-二林</option>
		<option value="33">彰化縣-彰化</option>
		<option value="34">彰化縣-線西</option>
		<option value="69">南投縣-竹山</option>
		<option value="36">南投縣-南投</option>
		<option value="72">南投縣-埔里</option>
		<option value="37">雲林縣-斗六</option>
		<option value="38">雲林縣-崙背</option>
		<option value="83">雲林縣-麥寮</option>
		<option value="41">雲林縣-臺西</option>
		<option value="40">嘉義縣-朴子</option>
		<option value="39">嘉義縣-新港</option>
		<option value="59">屏東縣-屏東</option>
		<option value="61">屏東縣-恆春</option>
		<option value="60">屏東縣-潮州</option>
		<option value="62">臺東縣-臺東</option>
		<option value="80">臺東縣-關山</option>
		<option value="63">花蓮縣-花蓮</option>
		<option value="78">澎湖縣-馬公</option>
		<option value="75">連江縣-馬祖</option>
		<option value="77">金門縣-金門</option>
'''

