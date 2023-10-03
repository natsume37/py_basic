# # import requests
# # from requests.auth import HTTPBasicAuth
# #
# # # url = 'https://ssr3.scrape.center'
# # # res = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
# # # print(res.status_code)
# # #
# #
# # proxies = {
# #     'http': "http:10.10.10.10:1080",
# #     'https': "https://10.10.10.10:1080"
# # }
# #
# # requests.get(url, proxies=proxies)
#
# import httpx
# # 声明开启http2.0模式
# client = httpx.Client(http2=True)
#
# url = 'https://spa16.scrape.center/'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
# }
# res = client.get(url, headers=headers)
# print(res.status_code)
# print(res.headers)
# print(res.text)
# res = httpx.get()
# res = httpx.post()
# res = httpx.delete()
# res = httpx.patch()
#
# res.text
# res.json()
# res.content
# res.headers
# res.status_code

import httpx
headers = {'User-Agent': 'my-app/0.0.1'}
with httpx.Client(headers=headers) as client:
    res = client.get('https://www.httpbin.org/get')
    print(res.json()['headers']['User-Agent'])
# my-app/0.0.1
# 用法等价于

# import httpx
#
#
# client = httpx.Client()
# try:
#     res = client.get('https://www.httpbin.org/get')
# finally:
#     client.close()