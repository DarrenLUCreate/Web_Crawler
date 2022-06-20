import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('D:/HappyCoder/python_training/Taoyuan_loc.csv',encoding='Big5')
df = pd.DataFrame(data)
df1 = pd.DataFrame({'Region':df['區域別'],'Sex':df['性別'],'Population':df['人口數']})
df2 = pd.DataFrame({"Region":df['區域別'],'Abroad':df['遷入人數自國外'],'NewTaipei':df['遷入人數自他省市新北市'],'Taipei':df['遷入人數自他省市臺北市'],'Taichung':df['遷入人數自他省市臺中市'],'Tainan':df['遷入人數自他省市臺南市'],'Kaoshiung':df['遷入人數自他省市高雄市']})
df3 = pd.DataFrame({"Region":df['區域別'],'Gender':df['性別'],'Population':df['人口數'],'Abroad':df['遷入人數自國外'],'NewTaipei':df['遷入人數自他省市新北市'],'Taipei':df['遷入人數自他省市臺北市'],'Taichung':df['遷入人數自他省市臺中市'],'Tainan':df['遷入人數自他省市臺南市'],'Kaoshiung':df['遷入人數自他省市高雄市'],"Total_immigration":df2.sum(axis = 1, skipna = True)})

df4 = df3.groupby(['Region']).sum()
#桃園每個區域的移入狀況跟人口總數

df4.describe()
#藉由describe()可以得知每個欄位的最大最小值以及四分位數、平均數、標準差

df4.sort_values(['Total_immigration'],ascending=False)
#龜山區為最多人移入的行政區，尤其以新北為大宗，復興區為最少人移入的行政區

ratio_immigration = (df4['Total_immigration']/df4['Population'])* 1000
#根據人口移入的公式計算每個區域移入人口佔總體人口的千分比

north = df4.sort_values(['NewTaipei'],ascending=False)
#可以看到台中、台南、高雄以及國外的移入人口首選都是桃園區，可以進一部探討為何南部跟北部移入人口的選擇角度


#製作移入人口圓餅圖

plt.figure(figsize=(12,8))
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

labels = df4.index
size = df4['Total_immigration']
plt.pie(size,
        labels = labels,
        autopct = "%1.1f%%",
        pctdistance = 0.6,
        textprops = {"fontsize":10},
        shadow=True)

plt.axis('equal')
plt.title("Pie chart of Immigration",{"fontsize":15})
plt.legend(loc='best')
plt.show()


#探討性別對於區域選擇的喜好
female = df3[df3['Gender']=='女']
female_sort = female.sort_values(['Total_immigration'],ascending=False)

male = df3[df3['Gender']=='男']
male_sort = male.sort_values(['Total_immigration'],ascending=False)

#male_sort.tail(3)
#female_sort.tail(3)
#male_sort.head(3)
#female_sort.head(3)
