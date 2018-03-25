from lxml import html
import time
tree=html.fromstring(open('C:/Users/lugengzhe/Desktop/HtmlPage3.html', 'r',encoding='UTF-8').read())
def sortHtml2obj():
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

        