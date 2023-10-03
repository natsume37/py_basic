# coding : utf-8
# 夏目&青一
# @name:03-项目实战
# @time: 2023/3/5  15:43
import requests
import re

url = 'https://ssr1.scrape.center/page/'

urls = [url + str(i) for i in range(1, 10)]
links = []


def reptile(link):
    res = session.get(link)
    # 获取所有的links
    link_end = re.findall('<a.*?href="(.*?)".*?class="name">', res.text)
    ur = 'https://ssr1.scrape.center'
    lin = [ur + i for i in link_end]
    for u in lin:
        links.append(u)


def detail(link):
    res = session.get(link)
    name = re.search('<h2.*?class="m-b-sm">(.*?)</h2>', res.text).group(1)
    type = re.findall('<button.*?<span>(.*?)</span>.*?</button>', res.text, re.S)[:-1]
    conment = re.search('<p data-v-63864230="" class="score m-t-md m-b-n-sm">(.*?)</p>', res.text)



if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    session = requests.Session()
    session.headers.update(headers)
    for i in urls:
        reptile(i)
    detail(links[0])
