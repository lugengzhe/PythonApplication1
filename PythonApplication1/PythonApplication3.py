import requests
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
sys.stdout = io.TextIOWrapper(sys.stdout,encoding='utf8')
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)
 
url=r"https://www.pin1111.com/zh-cn/"
browser.get(url)
browser.implicitly_wait(3)
print(browser.page_source.encode('utf-8').decode())
username=browser.find_element_by_name('CustomerId')
username.sent_keys('GL820429')
password=browser.find_element_by_name('Password')
password.sent_keys('LGZ425380_')
login_button = browser.find_element_by_id('loginButton')
login_button.submit()
browser.save_screenshot('picture1.png')
print(browser.page_source.encode('utf-8').decode())
browser.quit()