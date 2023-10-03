# coding : utf-8
# 夏目&青一
# @name:01-request
# @time: 2023/3/5  9:43
from bs4 import BeautifulSoup
import requests

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")
tags = soup.select('#content > div > div.article > ol')
for i in tags:
    res = i.select('div > div.info > div.hd > a > span:nth-child(1)')
    for i in res:
        print(i.get_text())