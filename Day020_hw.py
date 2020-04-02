# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:33:04 2020

Wikipedia爬蟲練習

@author: chenlw
"""
import requests
url = 'https://taqm.epa.gov.tw/taqm/tw/MonthlyAverage.aspx'
payload = {
    'ctl05$ddlSite': 58,
    'ctl05$ddlYear': 2019,
    'ctl05$btnQuery': '查詢',
    'ScriptManager1': 'ctl05$UpdatePanel1|ctl05$btnQuery',
    '__VIEWSTATE': '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',
    '__VIEWSTATEGENERATOR': '0C858E1A',
    '__EVENTVALIDATION': 'gEpZUOTcabNNcblKBVaWr0ElIeZplRIkETTXAbnBanuNYFa2PC2GrSLOB8T6jT2fNu8Y5BmrSZgI8678gNe76TyrO4oE23DGtaHdRUp2cNCQUsrwZVBZphtckmsnCucYskQxfxmTgA+qWyvQkOKUEVJLFR0lpVgrG01twnJGNEQrq2bsGyv9SOgEdiO4z4NN730wGpletad0hB8BBn3eA2PbrBgAa3ej96TgaZDTMF4pwSgl8U5Y2155qQtVWQw5+/6doRKCwvlgMYfRwAAO7DNMQplBC49mMhYJpRcACjdiK03L2ed++6zPPx7AteuooZnMSbGiAY8Y9sJFtK8+vumO3WpkjI7ntzgGVB+IgiVx8Xlqi8jBJ0oWLCofsARCtIUquDsAbs0ARBTdS1M4WFMn5MP/cfU8zMDC78Qbi+Eihh+ueM5DR+fq7LR0wQixgwuXwy2B8AcHCgYR46a+Wxz1951lmFdlVsFCWFCUUTRdDvT3XBxtG/ORp76vIHk3k0xe2cg24+F3TvG1AYHsyCdv4e+3hCCXaT4c1q+O7YovGApY2sgF/tE172fF2BRj+qLe5kUTxY6wrHxUqpFfxq8iTVth6Psaf3EjkAswyqBEibOfAWO2MQdvbLtoVX8MNNOp1Ew7Dj97gVSoKbOr/clDHvcBaNDUacF0twUdytQn+c0haup8CRT6/BQvdob4nTcrBSC+WUqGfjYtDMdElZW7aCOAWQEIU0HPLvbPnONJF8yNbOyXTAz2eYZhhxLle9ENiEXYzYDgDkJoPg+y7TvSLywx8aEVJvNJYvfAo4ybrgr6sbzJNwB3w82/oXibPVh96KEssJjtfrDubZ3Y5Xghus0xLvYT9uXRyXUWitMJn7LsCk8iWwrFk1lA0yf8z+x9NSiKVxFD/RNxCcM82ejzjqFxNDFlCUwOwVmbVPK/GQ9LQ08+Ih0j/t+XhoPfnpD5afdsXy9bhnQLfqia0NsenMw='
}
r = requests.post(url, data=payload)
r.status_code

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', class_='TABLE_G')
print(table)

import pandas as pd
d = pd.read_html(r.text)

import pandas as pd
print(pd.DataFrame(d[5]))




'''
解答版
d = {}
for tr in table.find_all('tr')[1:]:

    for i, td in enumerate(tr.find_all('td')):
        
        if len(tr.find_all('td')) == 5:
            if i == 0:
                obs = td.text
                d.setdefault(obs, {})
            if i == 2:
                date = td.text
            if i == 3:
                value = td.text
                d[obs][date] = value
        
        if len(tr.find_all('td')) == 3:
            if i == 0:
                date = td.text
            if i == 1:
                value = td.text
                d[obs][date] = value
print(d)
'''



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

