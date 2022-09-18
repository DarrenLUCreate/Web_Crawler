from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# Create your views here.

def main(request):

    return render(request, 'index.html', locals())


def HumanPostCrawl(request):
    keyword = request.POST["title"]

    option = Options()
    prefs = {
        'profile.default_content_setting_values' :
        {
            'notifications' : 2
        }
    }
    option.add_experimental_option('prefs',prefs)
    option.add_argument("--headless")
    option.add_argument("--incognito")

    browser_path = ''
    browser = webdriver.Chrome(browser_path, options=option)

    site_path = 'https://www.104.com.tw/jobs/main/'
    browser.get(site_path)

    human_title = '104人力銀行－不只找工作、幫你找方向的求職徵才平台'
    WebDriverWait(browser, 5, 0.5).until(EC.title_is(human_title))

    if keyword:
        WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.ID, 'ikeyword')))

        search_input = browser.find_element(By.ID, 'ikeyword')
        search_input.send_keys(keyword)
        search_btn = browser.find_element(By.XPATH, '/html/body/article[1]/div/div/div[4]/div/button')

        actions = ActionChains(browser)
        actions.move_to_element(search_btn)
        actions.click(search_btn)
        actions.perform()

        for i in range(1,2):
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)
        
        blocks = browser.find_elements(By.CLASS_NAME, 'b-block__left')
        all_jobs = []
        for block in blocks:
            title = block.find_element(By.CLASS_NAME, 'b-tit').text
            company = block.find_element(By.CLASS_NAME, 'b-list-inline').text
            area_info = block.find_element(By.CLASS_NAME, 'job-list-intro').text
            location = area_info[0:6]
            salary = block.find_element(By.CLASS_NAME, 'b-tag--default').text

            job_details = {'title': title, 'company': company, 'location': location, 'salary': salary}
            all_jobs.append(job_details)
        
        all_jobs = all_jobs[3:]

        return render(request, 'JobsResult.html', locals())
