import ssl
import datetime
import pymssql
from lxml import html
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
ssl._create_default_https_context = ssl._create_unverified_context # 全局取消证书验证
username = 'CZ868895'
password = '@Zcd1992'
LoginUrl = 'https://52.48.89.151:16869/zh-CN'
LoginElement = "//div[@id='body-container']/header/div[2]/div/span[2]/div[2]/div[1]/div/form/div/div[1]/div[1]/div[2]/div[2]/input"
LogoutUrl = 'https://52.48.89.151:16871/Sportsbook/Asia/zh-CN/Bet/E%20Sports/Live/Double/null/null/Regular/SportsBookAll/Decimal/77/#tab=Ticket&sport=&ticket=/Sportsbook/BetList/GetMini/7__customerId--GL820429&wager=/Sportsbook/BetList/GetMini/6__customerId--GL820429&line=/Sportsbook/Bet/Add/836017593/0/0/1/0/1.2__line--'
LogoutElement = "/html/body/div/p[1]/a"
#IngUrl = 'https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/en-GB/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/'
IngUrl = 'https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/null/Regular/SportsBookAll/Decimal/79'
IngElement = "//*[@id='12']/div[1]/h2"
info = []
class SingleObj(object):
    def __init__(self):
        super(SingleObj,self).__init__()
class GroupObj(object):
    def __init__(self):
        super(GroupObj,self).__init__()
def init():
    psOptions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='D:\Python\chromedriver.exe',chrome_options=psOptions)
    driver.set_window_size(480, 760)
    return driver
def login():
    driver.execute_script("document.getElementsByClassName('customerId')[0].value=arguments[0]",username)
    print('成功填入账户')
    driver.execute_script("document.getElementsByClassName('password')[0].value=arguments[0]",password)
    print('成功填入密码')
    driver.execute_script("document.getElementById('loginControlsButton').click()")
    print('成功跳转')
def reloadhtml():
    is_element_exist(IngElement,IngUrl)
def is_element_exist(target,url):
    s = driver.find_elements_by_xpath(target)
    if len(s) == 0:
        driver.get(url)
        is_element_exist(target,url)
def sortHtml2obj():
    global info
    tempTime=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    tree = html.fromstring(driver.page_source)
    matchinfo = []
    info = []
    count = 0
    loadcount = 2
    singlematchinfo = SingleObj()
    esport_todaymatch = tree.xpath("//div[contains(@class,'MarketContainer') and contains(@class,'Today') and contains(@class,'enabled') and contains(@id,'Today')]/table/tbody[@class='LeagueContainer regular']")
    while(loadcount > 0):
        for tbody in esport_todaymatch:
            trsum = tbody.xpath("tr[contains(@class,'evRow')]")
            singlematchinfo.GamesContainerHeader = ''.join(tbody.xpath("tr[@class='GamesContainerHeader']/th/span[3]/text()"))#中文释意可能有歧义 后续改为纯英文
            for tr in trsum:
                if 'Select matches of' not in ''.join(tr.xpath("td[@class='teamId']/div[@class='Home ' or @class='Home fav' or @class='Home  fav']/text()")):
                    singlematchinfo.starttime = ''.join(tr.xpath("td[@class='time']/span[@class='hTime']/text()"))
                    singlematchinfo.hometeam = ''.join(tr.xpath("td[@class='teamId']/div[@class='Home ' or @class='Home fav' or @class='Home  fav']/text()"))
                    singlematchinfo.awayteam = ''.join(tr.xpath("td[@class='teamId']/div[@class='Away ' or @class='Away fav' or @class='Away  fav']/text()"))
                    singlematchinfo.ht00 = ''.join(tr.xpath("td[@class='moneyline'][1]/div[contains(@class,'Home')]/a/text()"))
                    singlematchinfo.at00 = ''.join(tr.xpath("td[@class='moneyline'][1]/div[contains(@class,'Away')]/a/text()"))
                    singlematchinfo.htspread = ''.join(tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T0')]/text()"))
                    singlematchinfo.atspread = ''.join(tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T2')]/text()"))
                    singlematchinfo.htspread00 = ''.join(tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T1')]/a/text()"))
                    singlematchinfo.atspread00 = ''.join(tr.xpath("td[@class='spread'][1]/div/div[contains(@class,'T3')]/a/text()"))
                    singlematchinfo.total = ''.join(tr.xpath("td[@class='total'][1]/div[1]/div[contains(@class,'T0')]/text()"))
                    singlematchinfo.overt = ''.join(tr.xpath("td[@class='total'][1]/div[1]/div[contains(@class,'T1')]/a/text()"))
                    singlematchinfo.undert = ''.join(tr.xpath("td[@class='total'][1]/div[2]/div[contains(@class,'T2')]/a/text()"))
                    #print(singlematchinfo.__dict__)
                    matchinfo.append(singlematchinfo.__dict__)
                    #print('---------------------------------------------------------------')
                    SqlString="INSERT INTO OddData VALUES('pinnacle','"+singlematchinfo.GamesContainerHeader+"','none','none','"+singlematchinfo.starttime+"','"+singlematchinfo.hometeam+"','"+singlematchinfo.awayteam+"','"+singlematchinfo.ht00+"','"+singlematchinfo.at00+"','"+singlematchinfo.htspread+"','"+singlematchinfo.atspread+"','"+singlematchinfo.htspread00+"','"+singlematchinfo.atspread00+"','"+singlematchinfo.total+"','"+singlematchinfo.overt+"','"+singlematchinfo.undert+"','"+tempTime+"')"
                    cursor.execute(SqlString)
                    count = count + 1
                    connection.commit()
        loadcount = loadcount - 1
        esport_todaymatch = tree.xpath("//div[contains(@class,'MarketContainer') and contains(@class,'Early') and contains(@class,'enabled') and contains(@id,'Early')]/table/tbody[@class='LeagueContainer regular']")
    print(count)
    info.append(tempTime)
    info.append(matchinfo)
    print(info)
def weakreloadhtml():
    global LastTime
    NowTime=datetime.datetime.now()
    D_time=NowTime-LastTime
    if(D_time.seconds>250):
        LastTime = NowTime
        while len(driver.find_elements_by_xpath("//*[@id='SelectLeagues']/form/div[1]/div[5]/a"))==0:
            driver.execute_script("document.getElementById('SelectLeaguesButton').click()")
            sleep(2)
        driver.execute_script("document.getElementById('SelectLeagues').getElementsByTagName('form')[0].getElementsByClassName('Bar')[0].getElementsByClassName('SelectAll')[0].getElementsByClassName('sLeagBtn')[0].click()")
        driver.execute_script("document.getElementById('SelectLeagues').getElementsByTagName('form')[0].getElementsByClassName('Bar')[0].getElementsByClassName('Ok')[0].getElementsByTagName('input')[0].click()")
        driver.execute_script("document.getElementById('menuEventFilter_12_121').click()")
        sleep(5)
        while(driver.find_elements_by_xpath('//*[@id="lines"]/div[1]/div[1]/h2')[0].text!='E SPORTS'):
            driver.get('https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/null/Regular/SportsBookAll/Decimal/77')
    driver.execute_script("document.getElementById('Today_12').getElementsByClassName('market_header')[0].getElementsByClassName('puls')[0].getElementsByTagName('a')[0].click()")
    driver.execute_script("document.getElementById('Early_12').getElementsByClassName('market_header')[0].getElementsByClassName('puls')[0].getElementsByTagName('a')[0].click()")
def pull2bottom():
    latestheight = driver.execute_script("return document.body.scrollHeight")
    endheight = 0
    while(latestheight != endheight):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        sleep(2)
        endheight = latestheight
        latestheight = driver.execute_script("return document.body.scrollHeight")
def checkinformation():
    print('check')
    loginStatus = driver.find_elements_by_xpath(LoginElement)
    logoutStatus = driver.find_elements_by_xpath(LogoutElement)
    IngStatus = driver.find_elements_by_xpath(IngElement)
    if len(logoutStatus) > 0:
        print('登出状态')
        driver.get(LoginUrl)
        print('跳转登录页面')
        return
        print('重新check')
    else:
        if len(loginStatus) > 0:
            print('登录状态')
            login()
            print('登录成功')
            return
        else:
            if len(IngStatus) > 0:
                weakreloadhtml()
                print('刷新Odd成功')
                pull2bottom()
                sortHtml2obj()
                return
            else:
                reloadhtml()
                print('reload成功')
                return
if __name__ == '__main__':
    driver = init()
    connection=pymssql.connect(server='DESKTOP-I5UTC29',user='sa',password='4253805lgz',database='OddSQL')
    cursor=connection.cursor()
    driver.get(LoginUrl)
    LastTime=datetime.datetime.now()
    while(1):
        checkinformation()
    driver.quit()
    print('已结束')
    #driver.get('https://52.48.89.151:16871/Sportsbook/Asia/zh-CN/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/zh-CN/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/')#中文版
    #driver.get('https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/en-GB/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/')#英文版
    #driver.get(LoginUrl)#这一步特别缓慢 不全加载完
    #WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='body-container']/header/div[2]/div/span[2]/div[2]/div[1]/div/form/div/div[1]/div[1]/div[2]/div[2]/input")))
    #elem = driver.find_element_by_xpath("//input[@class='password' and @placeholder]")
    #elem.send_keys(password)
    #elem = driver.find_element_by_xpath("//a[@id='loginControlsButton']");
    #elem.send_keys(Keys.ENTER)#visible 方法登录