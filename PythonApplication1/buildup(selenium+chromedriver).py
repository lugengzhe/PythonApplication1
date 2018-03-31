import ssl
from lxml import html
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
ssl._create_default_https_context = ssl._create_unverified_context # 全局取消证书验证
def init():
    psOptions=webdriver.ChromeOptions()
    #psOptions.set_headless()
    driver=webdriver.Chrome(executable_path='D:\python\selenium\webdriver\chromedriver\chromedriver.exe',chrome_options=psOptions)
    return driver
def login():
    username = 'CZ868895'
    password = '@Zcd1992'
    url='https://52.48.89.151:16869/zh-cn'
    driver.set_window_size(480, 760)
    driver.get(url)#这一步特别缓慢 不全加载完
    #WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@class='customerId' and @placeholder]")))
    #elem=driver.find_element_by_xpath("//input[@class='customerId' and @placeholder]")
    WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='body-container']/header/div[2]/div/span[2]/div[2]/div[1]/div/form/div/div[1]/div[1]/div[2]/div[2]/input")))
    #elem=driver.find_element_by_xpath("//div[@id='body-container']/header/div[2]/div/span[2]/div[2]/div[1]/div/form/div/div[1]/div[1]/div[2]/div[2]/input")
    #elem.send_keys(username)
    driver.execute_script("document.getElementsByClassName('customerId')[0].value=arguments[0]",username)
    print('成功填入账户')
    #elem = driver.find_element_by_xpath("//input[@class='password' and @placeholder]")
    #elem.send_keys(password)
    driver.execute_script("document.getElementsByClassName('password')[0].value=arguments[0]",password)
    print('成功填入密码')
    #elem = driver.find_element_by_xpath("//a[@id='loginControlsButton']");
    #elem.send_keys(Keys.ENTER)#visible 方法登录
    driver.execute_script("document.getElementById('loginControlsButton').click()")#js方法登录
    print('成功跳转')
def sortHtml2obj():
    tree=html.fromstring(driver.page_source)
    count=0
    loadcount=2
    class Obj(object):
        def __init__(self):
            super(Obj,self).__init__()
    singlematchinfo=Obj()
    esport_todaymatch=tree.xpath("//div[contains(@class,'MarketContainer') and contains(@class,'Today') and contains(@class,'enabled') and contains(@id,'Today')]/table/tbody[@class='LeagueContainer regular']")
    while(loadcount>0):
        for tbody in esport_todaymatch:
            trsum=tbody.xpath("tr[contains(@class,'evRow')]")
            singlematchinfo.GamesContainerHeader=tbody.xpath("tr[@class='GamesContainerHeader']/th/span/text()")#中文释意可能有歧义 后续可改为纯英文
            for tr in trsum:
                singlematchinfo.starttime=tr.xpath("td[@class='time']/span[@class='hTime']/text()")
                singlematchinfo.hometeam=tr.xpath("td[@class='teamId']/div[@class='Home ' or @class='Home  fav']/text()")
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
def reloadhtml():
    #driver.get('https://52.48.89.151:16871/Sportsbook/Asia/zh-CN/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/zh-CN/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/')
    driver.get('https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/en-GB/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/')#英文版
    sleep(3)

    #flag=WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='menuSport_12']/a")))
    #print(flag)
    try:WebDriverWait(driver,1,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='13']/div[1]/h2")))
    except BaseException as e: 
    else:pull2bottom()
    
def weakreloadhtml():
    driver.execute_script("document.getElementById('Today_12').getElementsByClassName('market_header')[0].getElementsByClassName('puls')[0].getElementsByTagName('a')[0].click()")
    driver.execute_script("document.getElementById('Early_12').getElementsByClassName('market_header')[0].getElementsByClassName('puls')[0].getElementsByTagName('a')[0].click()")
def pull2bottom():
    latestheight=driver.execute_script("return document.body.scrollHeight")
    endheight=0
    while(latestheight!=endheight):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        sleep(2)
        endheight=latestheight
        latestheight=driver.execute_script("return document.body.scrollHeight")
if __name__=='__main__':
    driver = init()
    login()
    reloadhtml()
    sortHtml2obj()
    sleep(20)
    try:
        print('已完成')
    finally:
        driver.quit()
        print('已结束')
