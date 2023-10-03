# coding : utf-8
# 夏目&青一
# @name:守护进程
# @time: 2023/3/3  15:02
import time
from multiprocessing import Process


def name(name):
    print(name, "还活着")
    time.sleep(3)
    print(name, "死了")


if __name__ == '__main__':
    p = Process(target=name, kwargs={"name": "妲己"})
    p.daemon = True  # 设置为守护进程，主进程死、守护进程立马也死
    p.start()
    time.sleep(1)
    print("纣王死了")
