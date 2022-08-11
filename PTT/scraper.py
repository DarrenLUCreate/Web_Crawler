import aiohttp
import asyncio
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from aiohttp import TCPConnector


async def scraper(keyword):
    driver = webdriver.Chrome("./chromedriver.exe")
    url = "https://www.ptt.cc/bbs/"
    target_url = f'{url}{keyword}/index.html'
    driver.get(target_url)
    driver.add_cookie({'name': 'over18', 'value': '1'}) # 繞過已滿18歲的阻擋頁面
    driver.get(target_url)

    urls = []
    titles = []
    authors = []
    search_result = driver.find_elements(By.CLASS_NAME, "r-ent")
    

    for item in search_result:
        try:
            title = item.find_element(By.CLASS_NAME, 'title').text
        except NoSuchElementException:
            title = ''
        try:
            url = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except NoSuchElementException:
            url = ''
        try:
            author = item.find_element(By.CLASS_NAME, 'author').text
        except NoSuchElementException:
            author = ''

        urls.append(url)
        titles.append(title)
        authors.append(author)

    cookies = {'over18': '1'}
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False), cookies=cookies) as session: # 向每個連結發請求時，也會需要cookies以繞過已滿18歲的阻擋內容
        try:
            tasks = [asyncio.create_task(fetch_content(url, title, author, session)) for url, title, author in zip(urls, titles, authors)]
            await asyncio.gather(*tasks)
        except Exception as e:
            raise e

    return tasks
    

    
async def fetch_content(url, title, author, session):
    try:
        async with session.get(url) as response:
            html_body = (await response.text("utf-8", 'ignore'))
            soup = BeautifulSoup(html_body, 'lxml')
            content = soup.text

            result = {"url": url, 'title': title, 'author': author, 'content': content}

            return result
        
    except:
        result = {"url": url, 'title': title, 'author': author, 'content': None}

        return result


    


