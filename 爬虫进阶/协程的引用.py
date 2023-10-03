# coding : utf-8
# 夏目&青一
# @name:协程的引用
# @time: 2023/5/12  17:06

# url = 'https://www.httpbin.org/delay/5'

# import requests
# import time
#
# stat = time.time()
# for _ in range(1, 10):
#     print(time.time())
#     res = requests.get(url)
# end = time.time()
# print(end - stat)

# import asyncio
#
#
# async def execute(x):
#     print("number", x)
#
# coroutine = execute(1)
# print("oroutine", coroutine)
# print("结束1")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print("结束2")