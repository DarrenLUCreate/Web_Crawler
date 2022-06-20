# 桃園市111年4月人口移入情況

### Data_Description:
本次使用政府公開資料平台上，111年4月桃園人口動態登記資料，探討外來人口流入桃園市的情況  
使用的資料集為_: [111年4月桃園人口與戶籍動態登記](https://data.gov.tw/dataset/155575)  
使用的資料如下:  
* 區域(Region)
* 性別(Gender)
* 總人口數(Population)
* 移入人口來自國外(Abroad)
* 移入人口來自新北(NewTaipei)
* 移入人口來自台北(Taipei)
* 移入人口來自台中(Taichung)
* 移入人口來自台南(Tainan)
* 移入人口來自高雄(Kaoshiung)

### Explore Data Analysis
**1. 初步分析**  
由於定義的主題為人口流入的情況，我將資料使用Pandas做成移入的人口的資料表df_total_gender如下圖所示:  
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/df3.png)
  
接著我使用groupby函數將區域的男性與女性合併，即可以看到所有區域人口移入桃園的情況，為df_total_immigration
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/%E6%A1%83%E5%9C%92%E4%BA%BA%E5%8F%A3%E7%B8%BD%E8%A1%A8.png)
我們可以發現龜山區並非為桃園市的核心區域，但移入人口卻比桃園區以及中壢區高出許多，進一部探討各區的人口移入率
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/%E6%A1%83%E5%9C%924%E6%9C%88%E4%BA%BA%E5%8F%A3%E7%A7%BB%E5%85%A5%E7%8E%87.png)  
藉由人口移入率的公式: **(移入人口/總人口)X1000%**  
我們可以看到龜山區為千分之五遠高於其他的區域，與排名第二的桃園區，有著千分之四的差距 

****
**2. 外來人口選擇偏好**  
接著我想要探討南北是否對於區域的選擇有所不同，我使用sort_values對df_total_immigration進行排序分析可以得到以下兩張圖  
**北部**  
![北部](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/north.png)  
**南部**  
![南部](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/south.png)  
意外的是，我們可以看到北部以及南部對於區域的選擇確實有所不同，北部的第一名為龜山區，南部的第一名為桃園區   
進一步觀察桃園市的行政區域**桃園市行政區域劃分**    
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/800px-Taoyuan_City_Map_Chinese_Ver.png)  
目前的猜測式由於龜山區接壤雙北生活圈，交通便利，房價也相對雙北低廉，使得多數雙北區域的外來人口多選擇龜山區作為落腳地。  
而桃園區為桃園市的政經中心，生活機能便捷，工作機會也相對多，使得大多數的南部外來人口多選擇桃園區為落腳地。  
為了得到更有利的證據，之後可以利用爬蟲進一步優化這個研究。  

****

**3. 性別對於區域的選擇偏好**  
接著我想觀察性別是否也有對於區域的選偏好，我將df_total_gender依照性別拆分為2子資料集  
並使用sort_values觀察兩資料集的前三名以及後三名  
**女性的前三名**  
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/female_head.png)  
**女性的後三名**  
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/female_tail.png)  
**男性的前三名**  
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/male_head.png)  
**男性的後三名**  
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/male_tail.png)  

可以看到男女對於區域的選擇並無不同，大多都是選擇龜山區、桃園區、中壢區等生活機能便捷的地方作為居住地。

****
**人口區域對於移入人口派形圖**  
![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/%E6%A1%83%E5%9C%92%E7%A7%BB%E5%85%A5%E5%9C%93%E9%A4%85%E5%9C%96.png)  
上圖為使用matplotlib製作的外來人口居住區域派形圖，最大宗分別為:  
1. 龜山區(25.2%)
2. 桃園區(21.4%)
3. 中壢區(14.9%)  
這三個大區佔了總體外來人口的61.5%




