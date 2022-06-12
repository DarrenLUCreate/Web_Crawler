import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user_agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/101.0.1'
}

url = 'https://www.ptt.cc/bbs/Baseball/index.html'
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'html.parser')
items = soup.select('.r-ent')
row_list = []
for item in items:
    title = item.select('.title a')[0].text
    author = item.select('.author')[0].text
    data = {}
    data['title'] = title
    data['author'] = author
    row_list.append(data)

print(data)

headers = ['title','author']
with open('D:/HappyCoder/python_training/ptt_crawler.csv','w',encoding='utf-8') as f:
    dict_writer = csv.DictWriter(f,headers)
    dict_writer.writeheader()
    dict_writer.writerows(row_list)
    
