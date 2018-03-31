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
    url='https://www.vfacai.com/index.html#/gb_sports'
    #url='https://msp2.vfacai.com/Sports/Asia/Index.aspx?tpid=001&token=c9a59306b21ec3283918bfc53888f1294c781ace43b9521c3c3cc49c7c545058d228dd4ec69e1d2413fa7cb6dc43282dce406bdb3409e525f3bd683849647e8de4854aaa2ba50478920af4659dbf4374a135399cbf7bd7b7884eb3cf12940e28&languagecode=zh-cn&guest=login&oddstype=00001&sc='
    driver.set_window_size(480, 760)
    driver.get(url)#这一步特别缓慢 不全加载完
    WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='nav']/div[2]/a")))
    driver.execute_script("document.getElementById('a_menu_sub_00111_1_-1').click()")
    print('成功点开电子竞技')
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
    WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='AvailableBalance']/tbody/tr/td[2]/a[1]")))
    pull2bottom()
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
