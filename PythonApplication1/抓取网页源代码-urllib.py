import urllib.request
import requests
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context # 全局取消证书验证
url = r"https://www.pin1111.com/zh-cn/rtn"
url = r"http://60.162.152.114:8081/"
url=r'https://52.48.89.151:16869/zh-cn/'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode()
 