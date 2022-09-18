from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random
import time
import requests
import json
import configparser


browser_path = ''

class InstagramScraper():
    def __init__(self, keyword=str, account=str):
        self.keyword = keyword
        self.account = account
        self.config = configparser.ConfigParser()
        self.browser = webdriver.Chrome(browser_path)
        self.MIN_WAIT = 1
        self.MIDIUM_WAIT = 5
        self.MAX_WAIT = 10

    
    def InstagramSeleniumScraper(self):
        self.config.read('C:/Users/User/scraper/config.ini')
        USERNAME = self.config['Instagram']['USERNAME']
        PASSWORD = self.config['Instagram']['PASSWORD']

        ig_login_path = 'https://www.instagram.com/'
        self.browser.get(ig_login_path)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        start_time = time.time()

        user_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')
        submit_btn = self.browser.find_element(By.CLASS_NAME, 'L3NKy')

        # 登入IG
        action = ActionChains(self.browser)
        action.move_to_element(user_input)
        action.click()
        action.send_keys(USERNAME)
        time.sleep(random.uniform(self.MIN_WAIT, self.MIDIUM_WAIT))
        action.move_to_element(password_input)
        action.click()
        action.send_keys(PASSWORD)
        time.sleep(random.uniform(self.MIN_WAIT, self.MIDIUM_WAIT))
        action.move_to_element(submit_btn)
        action.click()
        action.perform()

        time.sleep(random.randint(self.MIDIUM_WAIT,self.MAX_WAIT))

        # 追蹤
        if self.keyword == 'follow':
            account_path = f'https://www.instagram.com/{self.account}/'
            self.browser.get(account_path)
            self.browser.implicitly_wait(5)

            check_list = [
                {'follow_method': By.CLASS_NAME,'follow_target': '_acas'},
                {'follow_method': By.XPATH, 'follow_target': '//*[@id="mount_0_0_yQ"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]/div/div[2]/button'}
            ]
            try:
                for check in check_list:
                    follow_btn = self.browser.find_element(check['follow_method'], check['follow_target'])
                    if follow_btn:
                        follow_btn.click()
                        break

            except NoSuchElementException:
                print('Can not find element !')

        # 退追蹤
        if self.keyword == 'unfollow':
            account_path = f'https://www.instagram.com/{self.account}/'
            self.browser.get(account_path)
            self.browser.implicitly_wait(5)
            
            check_list = [
                {'unfollow_method': By.CLASS_NAME,'unfollow_target': '_ab9x',
                 'confirm_method': By.CLASS_NAME, 'confirm_target': '_a9-_'},
                {'unfollow_method': By.XPATH,'unfollow_target': '//*[@id="mount_0_0_qt"]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button/div',
                 'confirm_method': By.XPATH, 'confirm_target': '//*[@id="mount_0_0_qt"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]'}
            ]

            try:
                for check in check_list:
                    unfollow_btn = self.browser.find_element(check['unfollow_method'], check['unfollow_target'])
                    unfollow_btn.click()
                    confirm_btn = self.browser.find_element(check['confirm_method'], check['confirm_target'])
                    confirm_btn.click()

            except NoSuchElementException:
                print('Can not find element !')        

        time.sleep(10)
        print(f'此次爬蟲總共花了 {time.time()-start_time} 秒')
        self.browser.quit()

    def get_media_info_data(self, count, after):
        pass



if __name__ == '__main__':
    a = InstagramScraper('follow', 'chloefit0612')
    a.InstagramSeleniumScraper()
