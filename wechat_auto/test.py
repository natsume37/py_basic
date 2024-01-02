# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: test
# @TIME: 2024/1/2 14:32
import requests

headers = {
    'Api-Key': 'bshpbitz47txrw7y',
    'Api-Secret': 'igz9b9dp',
    'Content-Type': 'application/json;charset=UTF-8'
}
payload = {
    "content": "你好",
    "type": 1,
    "from": "黄兄",
}

res = requests.post('https://api.mlyai.com/reply', headers=headers, json=payload)
print(res.json()['data'][0]['content'])
