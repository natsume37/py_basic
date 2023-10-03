# coding : utf-8
# 夏目&青一
# @name:02-BeautifulSoup库
# @time: 2023/3/4  19:50
# 导入 requests 库

import requests
from bs4 import BeautifulSoup

url =  'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
# 选取直接子节点(直接在这个标签里面的）
# contents
print(soup.head.contents)
# <meta content="cZdR4xxR7RxmM4zE" name="baidu-site-verification">
# <meta content="no-cache" http-equiv="Pragma"/>
# <meta content="Sun, 6 Mar 2005 01:00:00 GMT" http-equiv="Expires"/>
# ...