import requests
import sys
import io
import ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
data = {'CustomerId':'CZ868895', 
        'Password':'@Zcd1992', 
        'AppId':'Classic'}

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'https://52.48.89.151:16869/login/authenticate/Classic/en-GB'

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)

#登录后才能访问的网页
url = 'https://52.48.89.151:16871/Sportsbook/Asia/en-GB/Bet/E%20Sports/All%20Games/Double/null/0/Regular/SportsBookAll/Decimal/7/#tab=Menu&sport=/Sportsbook/Asia/zh-CN/GetLines/E%20Sports/All%20Games/1/null/0/Regular/SportsBookAll/Decimal/7/false/'

#发送访问请求
resp = session.get(url)

print(resp.content.decode('utf-8'))