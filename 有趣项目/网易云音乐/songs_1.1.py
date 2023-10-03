import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start=0&filter='


# 本网站反扒不是很高、请求头可以加点
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)
print(res.text)