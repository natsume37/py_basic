# coding : utf-8
# 夏目&青一
# @name:11-互斥锁
# @time: 2023/5/13  14:42
import random
from multiprocessing import Process, Lock
import json
import time


def search_tickets(name):
    with open('date/test03.json', 'r', encoding='utf-8') as f:
        count = json.load(f)
        print(f'{name}执行查询操作，余票为：{count["count"]}')
        return count


def buy_tickets(name):
    with open('date/test03.json', 'r', encoding='utf-8') as f:
        count = json.load(f)
        time.sleep(random.randint(1, 5))
        if count.get('count') > 0:
            count['count'] -= 1
            with open('date/test03.json', 'w', encoding='utf-8') as f:
                json.dump(count, f)
            print(f'用户：{name}，抢票成功')
        else:
            print(f'{name} 余票不足抢票失败')


def task(name, mutex):
    search_tickets(name)
    # 加锁
    mutex.acquire()
    buy_tickets(name)
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(1, 9):
        p = Process(target=task, args=(' ', mutex))
        p.start()
