import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user_agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/101.0.1'
}

url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,"lxml")
list1=[]
result = soup.find_all('div',class_='col-sm-12 newsItems')
for j in result:
    title = j.find('a',class_='gt').string
    list1.append(title)

list2 = []
time = soup.find_all('time',style='color: #a2a2a2;')
for i in time:
    times = i.string
    list2.append(times)

dict1 = dict(zip(list2,list1))
for key,value in dict1.items():
    print(key,value)


with open('D:/HappyCoder/python_training/news.json','w',encoding='utf-8') as f:
    json.dump(dict1,f,ensure_ascii=False)
