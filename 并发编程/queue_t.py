# coding : utf-8
# 夏目&青一
# @name:queue_线程安全
# @time: 2023/2/3  17:24

import requests
from bs4 import BeautifulSoup

urls = [
    f'https://www.cnblogs.com/#{i}'
    for i in range(1, 50 + 1)
]


def craw(url):
    res = requests.get(url)
    return res.text


def parser(html):
    # post-item-title
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post-item-title')
    return [(link['href'], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parser(craw(urls[4])):
        print(result)
