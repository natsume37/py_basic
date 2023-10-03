# coding : utf-8
# 夏目&青一
# @name:抢票
# @time: 2023/3/3  15:13
import json
from multiprocessing import Process, Lock
import time
import random


# 抢票

def search_ticket(name):
    # 读取文件
    with open("data/titakes", "r", encoding="utf-8") as f:
        dic = json.load(f)
    print(f'用户{name}查询余票：{dic.get("tickets_num")}')


# 买票
def buy_ticket(name):
    with open("data/titakes", "r", encoding="utf-8") as f:
        dic = json.load(f)
    time.sleep(random.randint(1, 5))
    if dic["tickets_num"] > 0:
        dic["tickets_num"] -= 1
        with open("data/titakes", "w", encoding="utf-8") as f:
            json.dump(dic, f)
        print(f'用户{name}买票成功,余票{dic["tickets_num"]}')

    else:
        print(f"余票不足，用户{name}买票失败")


def task(name, mutex):
    search_ticket(name)
    # 抢锁
    mutex.acquire()
    buy_ticket(name)
    # 释放锁
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()  # 定义互斥锁
    for i in range(1, 8):
        p = Process(target=task, args=(i, mutex))
        p.start()
