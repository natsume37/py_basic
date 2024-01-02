# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: test
# @TIME: 2023/11/10 19:28
token = '1a60e0a5e8045c1443221cbc245f5d62'
id = 'wx8ef0de5126c924d5'
url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={id}&secret={token}'
import requests
res = requests.get(url)
print(res.json())
