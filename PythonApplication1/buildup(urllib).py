import sys
import io
import urllib.request
import http.cookiejar
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
data = {'CustomerId':'CZ868895', 
        'Password':'@Zcd1992', 
        'AppId':'Classic'}
post_data = urllib.parse.urlencode(data).encode('utf-8')

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）    
login_url = 'https://52.48.89.151:16869/login/authenticate/Classic/en-GB'

#构造登录请求     
req = urllib.request.Request(login_url, headers = headers, data = post_data)

#构造cookie
cookie = http.cookiejar.CookieJar()

#由cookie构造opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

#发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
resp = opener.open(req)

#登录后才能访问的网页
url = 'https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/zh-CN/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/'

#构造访问请求
req = urllib.request.Request(url, headers = headers)

resp = opener.open(req)

print(resp.read().decode('utf-8'))