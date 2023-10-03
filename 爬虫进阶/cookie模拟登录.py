# coding : utf-8
# 夏目&青一
# @name:cookie模拟登录
# @time: 2023/3/5  9:53
import requests
from bs4 import BeautifulSoup

url = 'https://wpblog.x0y1.com/wp-login.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

data = {
    'log': 'codetime',
    'pwd': "shanbay520",
    'wp-submit': '登录',
    'redirect_to': 'https://wpblog.x0y1.com',
    'testcookie': '1',
}

# requests的cookie不共享，要手动传。
res = requests.post(url, data=data, headers=headers)
login_cookies = res.cookies

# 进入python文章分类、手动传参
py_url = 'https://wpblog.x0y1.com/?cat=2'
py_text = requests.get(py_url, cookies=login_cookies, headers=headers)

# 获取每篇文章的url
tags = BeautifulSoup(py_text.text, "html.parser")
link_a = tags.select('main#main h2 > a')
for i in link_a:
    print(i.text)

保持cookie