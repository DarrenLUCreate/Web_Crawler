from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import csv

s = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=s)
#由於DeprecationWarning警告的类型错误：该类型的警告大多属于版本更新时，所使用的方法过时的原因，他在当前版本被重构，还可以传入参数，但是在之后的某个版本会被删除.
#article url:https://blog.csdn.net/m0_62298204/article/details/120802053



driver.get('https://kma.kkbox.com/charts/daily/newrelease?terr=tw&lang=tc&category=297')
#發出網頁請求
page_content = driver.page_source
#取得網頁內容
#print(page_content) 觀察網頁內容
row_list = []
soup = BeautifulSoup(page_content,'html.parser')
#將HTML轉換成BeautifulSoup物件，解析器為html.parser
items = soup.select('.charts-list-row')
#所需物件都存在.charts-list-row裡
for item in items:
    song_list = {}
    rank = item.select('.charts-list-rank')[0].text
    name = item.select('.charts-list-song')[0].text
    artist = item.select('.charts-list-artist')[0].text
    song_list['song_rank'] = rank
    song_list['song_name'] = name
    song_list['artist'] = artist
    row_list.append(song_list)
#整理成dict丟入row_list裡

headers = ['song_rank','song_name','artist']
# 使用檔案 with ... open 開啟 write (w) 寫入檔案模式，透過 csv 模組將資料寫入。使用 utf-8 避免中文亂碼，並設定 newline 去除空白行
with open('./song.csv','w',newline='',encoding='utf-8')as f:
    dict_writer = csv.DictWriter(f,headers)
    dict_writer.writeheader()
    dict_writer.writerows(row_list)

#check是否有存取到csv裡
with open('./song.csv','r',newline='',encoding='utf-8')as i_f:
    rows = csv.reader(i_f)
    for row in rows:
        print(row)

   
time.sleep(1)
driver.quit()
