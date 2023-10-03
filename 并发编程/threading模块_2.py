# coding : utf-8
# 夏目&青一
# @name:threading模块_2
# @time: 2023/2/3  16:48

# 爬取博客园信息
import time
import threading

import requests

urls = [
    f'https://www.cnblogs.com/#{i}'
    for i in range(1, 50 + 1)
]


def craw(url):
    res = requests.get(url)
    print(res.status_code, len(res.text))


# 单线程爬取
def single_thread(url_list):
    print('single_thread begin')
    for url in urls:
        craw(url)
    print('single_thread began')


# 多线程爬取
def multi_thread(url_list):
    print('multi_thread begin')
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))
        )
    # 线程程开始
    for thread in threads:
        thread.start()
    # 线程等待结束
    for thread in threads:
        thread.join()

    print('multi_thread began')


single_thread_start = time.time()
single_thread(urls)
single_thread_end = time.time()

multi_thread_start = time.time()
multi_thread(urls)
multi_thread_end = time.time()

print(f'single_thread {single_thread_end - single_thread_start}')
print(f'multi_thread {multi_thread_end - multi_thread_start}')

# Result
# single_thread 15.876798868179321
# multi_thread 0.732025146484375
