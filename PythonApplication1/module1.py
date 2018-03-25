from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from time import sleep

username = 'CZ868895'
password = '@Zcd1992'
chrome_options = Options() 
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
url = 'https://52.48.89.151:16869/zh-cn/'
url = 'https://www.baidu.com'
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'D:\python\selenium\webdriver\chromedriver\chromedriver.exe')
driver.get('http://60.162.152.114:8081/')
sleep(10)
print('end')
print(driver.title)
print('end')
elem = driver.find_element_by_xpath(r'//*[@id="usercode"]')
print(elem)
sleep(1)
elem.send_keys(username)
print('成功填入')
usertext = selector.xpath(r'//*[@id="usercode"]')
print(usertext[0].xpath('string(.)').strip())
#elem = driver.find_element_by_xpath(r"//*[@id='loginPassword']");
#elem = driver.find_element_by_xpath(r"/html/body/div[3]/input[2]");
elem = driver.find_element_by_xpath(r'//*[@id="password"]')
print(elem)
elem.send_keys(password)