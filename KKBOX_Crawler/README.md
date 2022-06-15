# KKBOX華語新歌日排行榜

* 研究方法
  1. 設定爬取目標: 爬取標的為新歌的排行，歌名以及歌手，並輸出成Song.csv
  2. 觀察網頁: KKBOX應該是由AJAX寫成，先傳輸一個HTML，再由JS傳輸資料
  3. 發出請求:使用selenium的driver.page_source載入網頁內容，再轉成BeautifulSoup物件，並利用html.parser作為解析器
  4. 解析內容:使用BeauifulSoup的select進行解析
  5. 整理成資料儲存至csv裡
 
* 輸出畫面
