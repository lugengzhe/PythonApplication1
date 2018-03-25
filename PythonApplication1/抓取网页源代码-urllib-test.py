import urllib
import requests
import ssl 
import http
import urllib3
ssl._create_default_https_context = ssl._create_unverified_context # 全局取消证书验证
login_url=r'https://52.48.89.151:16869/zh-cn/'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/css,*/*;q=0.1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': '52.48.89.151:16869',
    'Referer': 'https://52.48.89.151:16869/zh-cn/cookiepolicy/index?&ui=desktop&referDomain=https://52.48.89.151:16869&w=860&h=600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
login_data = urllib.parse.urlencode({
                  #"fakeusernameremembered":'',
                  #"fakepasswordremembered":'',
                  "CustomerId":'CZ868895',
                  "Password":'@Zcd1992',
                  #"CustomerId":'GL820429',
                  #"Password":'LGZ425380_',
                  "AppId":'Classic'})
#login_data={
#        "Cookie": 'CustomerLicenseType=Curacao; domain=52.48.89.151; expires=Wed, 21-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'RealityCheck=1521526573418; domain=52.48.89.151; expires=Wed, 21-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'bootstraprun=no; domain=52.48.89.151; expires=Wed, 21-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'GRP=!5UC9X1zLvB/DO78CzDeCldF/EWDfBRHt3BZx/u9oiXSNLdy9gFUqCwsLsGkD; domain=52.48.89.151; expires=Mon, 18-Jun-2018 06:16:13 GMT; path=/',
#        "Cookie": 'SessionTimeout=; domain=52.48.89.151; expires=Mon, 19-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'UserAccess=0; domain=52.48.89.151; expires=Thu, 19-Apr-2018 06:16:13 GMT; path=/',
#        "Cookie": 'BrowserSessionId=6fcc678c-6f0f-4a8e-8795-effd6007bd96; domain=52.48.89.151; expires=Wed, 21-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'UserPrefsCookie=languageId=3&priceStyle=Decimal&linesTypeView=d&device=d&languageGroup=Classic&timeZoneId=7; domain=52.48.89.151; path=/',
#        "Cookie": 'RealityCheck=; domain=52.48.89.151; expires=Mon, 19-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'tempid=; domain=52.48.89.151; expires=Mon, 19-Mar-2018 06:16:13 GMT; path=/',
#        "Cookie": 'custid=id=CZ868895&login=201803192316&roundTrip=201803192316&hash=FA691DCED8EFFF9BB3FDA81DAF0F27D9; domain=52.48.89.151; expires=Tue, 20-Mar-2018 08:16:13 GMT; path=/'}
cj=http.cookiejar.CookieJar() #获取Cookiejar对象（存在本机的cookie消息）
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))#自定义opener,并将opener跟CookieJar对象绑定
urllib.request.install_opener(opener) #安装opener,此后调用urlopen()时都会使用安装过的opener对象
response=opener.open(login_url,login_data.encode(encoding='UTF8')).read()  #访问登录页，自动带着cookie信息]
print(response) #返回登陆后的页面源代码
print('头文件')
#for key in login_data: #增加多个header，把cookie放到header中，访问server时使用该cookie
#    print(key)
#    opener.addheaders.append((key,login_data[key]))

#print(opener.open(r'https://52.48.89.151:16871/Sportsbook/Asia/zh-CN/Bet/Soccer/Today/Double/null/null/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=').read())










#req = urllib.request.Request(url, headers=headers)
#response = urllib.request.urlopen(req)
#html = response.read().decode()
 