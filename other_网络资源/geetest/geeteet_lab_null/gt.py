import requests
import json
import re
from lxml import etree
import time
from http.cookies import SimpleCookie

register_url = "http://localhost:5000/pc-geetest/register?t=" + str(int(time.time()*1000))
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
# 1.取cookie 字符串
sess = requests.Session()
res = sess.get(register_url,headers=headers)
cookie_str = res.headers['Set-Cookie']
cookie = SimpleCookie(cookie_str)
cookies = {i.key:i.value for i in cookie.values()}
print(cookies)
print(res.text)

# 2. 访问主页
index_url = "http://localhost:5000"
res = sess.get(index_url,headers=headers,cookies=cookies)
print(res.cookies)
