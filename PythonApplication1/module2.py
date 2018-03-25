import os
from lxml import html  
from time import sleep #导入
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By   #导入
from selenium.webdriver.common.keys import Keys #导入
from selenium.webdriver.support.wait import WebDriverWait   #导入
from selenium.webdriver.support import expected_conditions #导入
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context # 全局取消证书验证
# 初始化配置
def sortHtml2obj(tree):
    count=0
    loadcount=2
    class Obj(object):
        def __init__(self):
            super(Obj,self).__init__()
    singlematchinfo=Obj()
    while(loadcount>0):
        esport_todaymatch=tree.xpath("//div[contains(@class,'MarketContainer') and contains(@class,'Today') and contains(@class,'enabled') and contains(@id,'Today')]/table/tbody[@class='LeagueContainer regular']")
        for tbody in esport_todaymatch:
            trsum=tbody.xpath("tr[contains(@class,'evRow')]")
            singlematchinfo.GamesContainerHeader=tbody.xpath("tr[@class='GamesContainerHeader']/th/span/text()")
            for tr in trsum:
                singlematchinfo.starttime=tr.xpath("td[@class='time']/span[@class='hTime']/text()")
                singlematchinfo.hometeam=tr.xpath("td[@class='teamId']/div[@class='Home fav']/text()")
                singlematchinfo.awayteam=tr.xpath("td[@class='teamId']/div[@class='Away ']/text()")
                singlematchinfo.ht00=tr.xpath("td[@class='moneyline'][1]/div[contains(@class,'Home')]/a/text()")
                singlematchinfo.at00=tr.xpath("td[@class='moneyline'][1]/div[contains(@class,'Away')]/a/text()")
                singlematchinfo.htspread=tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T0')]/text()")
                singlematchinfo.atspread=tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T2')]/text()")
                singlematchinfo.htspread00=tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T1')]/a/text()")
                singlematchinfo.atspread00=tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T3')]/a/text()")
                singlematchinfo.total=tr.xpath("td[@class='total'][1]/div[1]/div[contains(@class,'T0')]/text()")
                singlematchinfo.overt=tr.xpath("td[@class='total'][1]/div[1]/div[contains(@class,'T1')]/a/text()")
                singlematchinfo.undert=tr.xpath("td[@class='total'][1]/div[2]/div[contains(@class,'T2')]/a/text()")
                print(singlematchinfo.__dict__)
                print('---------------------------------------------------------------')
                count=count+1
        loadcount=loadcount-1
        esport_todaymatch=tree.xpath("//div[contains(@class,'MarketContainer') and contains(@class,'Early') and contains(@class,'enabled') and contains(@id,'Early')]/table/tbody[@class='LeagueContainer regular']")
    print(count)
def initWork():
    chromedriver = r'D:\python\selenium\webdriver\chromedriver\chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    return driver
# 执行登录
def handleLogin():
    # 定义自己的用户名密码
    #username = "15267051266"
    #password = "Lgz@94Cyy"
    username = 'CZ868895'
    password = '@Zcd1992'
    # 执行操作的页面地址
    #url = r'http://60.162.152.114:8081/'
    url=r'https://www.pin1111.com/zh-cn/rtn'
    url=r'https://52.48.89.151:16869/zh-cn/'
    #driver.set_window_size(480, 760)
    driver.get(url)
    print(driver.title)
    cookie1 = driver.get_cookies()
    # 将获得cookie的信息打印
    print('第一页')
    print(cookie1)
    # 下面就开始在打开的页面中自动执行操作了
    # 根据xpath获取登录按钮
    #elem = driver.find_element_by_xpath(r"/html/body/div[3]/input[1]");
    #elem=driver.find_element_by_xpath(r'//*[@id="loginMvc"]/form/div/div[1]/div[1]/div[2]/div[2]/input')
    WebDriverWait(driver,60,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,r'//*[@id="loginMvc"]/form/div/div[1]/div[1]/div[2]/div[2]/input')))
    elem=driver.find_element_by_xpath('//*[@id="loginMvc"]/form/div/div[1]/div[1]/div[2]/div[2]/input')
    print(elem)
    sleep(1)
    # 发送确认按钮跳转到登录页面
    #elem.send_keys(Keys.ENTER)
    # 休眠两秒钟后执行填写用户名和密码操作
    #elem = driver.find_element_by_xpath(r"//*[@id='loginName']");
    elem.send_keys(username)
    print('成功填入')
    #elem = driver.find_element_by_xpath(r"//*[@id='loginPassword']");
    #elem = driver.find_element_by_xpath(r"/html/body/div[3]/input[2]");
    elem = driver.find_element_by_xpath(r'//*[@id="loginMvc"]/form/div/div[1]/div[1]/div[3]/div[2]/input')
    print(elem)
    elem.send_keys(password)
    elem = driver.find_element_by_xpath(r'//*[@id="loginControlsButton"]');
    elem.send_keys(Keys.ENTER)
    sleep(5)
    cookie2 = driver.get_cookies()
    # 将获得cookie的信息打印
    print(cookie2)
    print('打印页面信息')
    driver.get('https://52.48.89.151:16871/Sportsbook/Asia/zh-CN/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/zh-CN/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/')
 
    sleep(30)
    handleScroll()
    print('断d')
    #soup = BeautifulSoup(driver.page_source, "lxml")
    sortHtml2obj(html.fromstring(driver.page_source))
    #print(driver.page_source)

    print('断d')
    #while 1 :
    #              print('断d')
    #              soup = BeautifulSoup(driver.page_source, "lxml")
    #              sleep(60)
                  
    #              print(soup)



    # 判断是否登录成功
    if cookie1 == cookie2:
        print(u'可能登录失败了')
        sleep(60)
# 执行滚动加载出全部内容      
def handleScroll():

    for i in range (1 , 7 , 1):
        Transfer_Clicks(driver)
        print (u'滚动%d次' % i)
        sleep(2)
    sleep(10)
# 定义一个滚动函数
def Transfer_Clicks(browser):
    try:
        browser.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
        # 这个是执行一段Javascript函数，将网页滚到到网页顶部。
        # browser.execute_script("window.scrollBy(0,5)", "")
        # 向下滚动200个像素，鼠标位置也跟着变了
        ActionChains(browser).move_by_offset(0,200).perform()
        # 向上移动鼠标80个像素，水平方向不同
        #ActionChains(browser).click().perform()
        # 鼠标左键点击
        #ActionChains(browser).key_down(Keys.TAB).perform()
        # 模拟tab键的输入
        #ActionChains(browser).send_keys(Keys.ENTER).perform()
        # 模拟输入ENTER键
    except:
        pass
    return "Transfer successfully \n"

if __name__ == '__main__':
    driver = initWork()
    elems = handleLogin()
  


    
