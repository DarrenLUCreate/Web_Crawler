# PTT文章標題爬取

## 練習目標:

1. 練習爬取PTT的文章標頭及作者
2. 觀察網站的結構

## 研究方法:

1. 首先觀察PTT的網站原始碼是否有我需要的資料。
2. 經過開發者工具可以看到有我所需要的資料分別是.tilte 跟.author的文字內容
![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/ptt_source.png)
3. 藉由發出http get向server端發送請求
4. 可以發向我所需要的資料都在.r-ent的class下，分別是.title跟.author
5. 將資料加上標頭，輸出成csv，並觀察其成果。
![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/ptt_output.png)
