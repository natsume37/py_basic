# coding : utf-8
# 夏目&青一
# @name:生产者消费者模型
# @time: 2023/3/3  16:46
import random
import time
from multiprocessing import Process, JoinableQueue


def producer(name, food, q):
    for i in range(5):
        time.sleep(random.randint(1, 4))
        print(f'{name}生产了{food}{i}')
        q.put(f'{food}{i}')


def consumer(name, q):
    while True:
        food = q.get()
        time.sleep(random.randint(1, 3))
        print(f'{name}吃了{food}')

        q.task_done()  # 告诉队列已经拿走了一个数据、并且已经处理完了


if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=("中华小当家", "黄金炒饭", q))
    p2 = Process(target=producer, args=("神厨小福贵", "佛跳墙", q))



    c1 = Process(target=consumer, args=("八戒", q))
    c2 = Process(target=consumer, args=("悟空", q))
    # 设置守护进程、准备陪葬
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()

    q.join()
    # 走到这一步说明：主进程已经死了、但需要子进程陪葬
    print("子进程开始陪葬")