# KKBOX華語新歌日排行榜

* 研究方法
  1. 設定爬取目標: 爬取標的為新歌的排行，歌名以及歌手，並輸出成Song.csv
  2. 觀察網頁: KKBOX應該是由AJAX寫成，先傳輸一個HTML，再由JS傳輸資料
  3. 發出請求:使用selenium的driver.page_source載入網頁內容，再轉成BeautifulSoup物件，並利用html.parser作為解析器
  4. 解析內容:使用BeauifulSoup的select進行解析
  5. 整理成資料儲存至csv裡
 
* 檢查網頁
![開發人員工具檢視網頁架構](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/KKbox_WEB.png)
* 輸出畫面
![CSV輸出畫面](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/KKbox_output.png)

* 遇到的問題
  1.使用selenium的時候會遇到很多錯誤，例如:
    * USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。
    * list index out of range
    * ResultSet object has no attribute 'find_all'
    * nameerror name 'by' is not defined selenium python
    * DeprecationWarning: find_elements_by_class_name is deprecated. Please use find_elements(by=By.CLASS_NAME, value=name) instead
  2. 以上都是我在Anaconda Prompt上執行時的報錯，還不是太了解這些錯誤的原因，大部分的問題有去搜尋網路上的source，以下是我搜尋的Solutions
  3. source:
    * nameError:'https://stackoverflow.com/questions/44629970/python-selenium-webdriver-name-by-not-defined'
    * DeprecationWarning:'https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium'
    * list index out of range:'https://stackoverflow.com/questions/12570329/selenium-list-index-out-of-range-error'
    * 'https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html'
  
 
   
