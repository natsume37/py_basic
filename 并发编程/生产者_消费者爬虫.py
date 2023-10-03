# coding : utf-8
# 夏目&青一
# @name:生产者_消费者爬虫
# @time: 2023/2/3  17:44

import threading
import time
import random
import queue
import queue_t


# 生产者模式
def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = queue_t.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f'craw {url}',
              'url.queue.size=', url_queue.qsize())
        time.sleep(random.randint(1, 2))


# 消费者模式
def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = queue_t.parser(html)
        for result in results:
            fout.write(str(result) + '\n')
        print(threading.current_thread().name, f'results.size', len(results),
              'html.queue.size=', html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    # urls,是链接代码列表
    for url in queue_t.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f'craw{idx}')
        t.start()

    fout = open('02.txt', 'w')
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name=f'parse{idx}')
        t.start()
