# 三立新聞網熱門文章標題的抓取

## 練習目標:

1. 主要目標: 想知道在由伺服器渲染而成網頁，Requests與BeautifulSoup的爬取效果
2. 主要爬取目標欄位: 文章的發布時間與文章的標題
3. 延伸目標: 可以透過情感分析與字詞分析，對於新聞的標題做整理，並製作新聞輿情文字雲

## 研究方法:

1. 觀察網頁: 我發現三立新聞網的網頁原始碼裡的主要爬取標的是可以找的到的，說明該網頁內容不是由JS動態輸出，而是由伺服器渲染而成
2. 使用開發者工具觀察網頁結構:
   ![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/obseve.png)
   由上圖可得知我的爬取標的包裹在class為"col-sm-12 newsItems"的div裡面，於是我將網頁框架做一個整理如下圖所示
   ---
   ![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/web_structure.png)
   
3. 使用requests套件發出http get的請求到server端。
4. 使用find_all對文章標題所在的class爬取裡面的內容，以及time標籤裡所需要的文章發布時間。
5. 最後將所需要的資料整理成字典，利用json.dump輸出成stn_crawler.json檔案，完成此次的爬蟲練習。
6. ![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/stn_output.png)

## 練習心得

透過此次練習，可以得知爬蟲基本的五步驟，另外可以比較select與find跟find_all的使用，達成一點小成就感!


