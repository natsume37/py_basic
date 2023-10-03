# coding : utf-8
# 夏目&青一
# @name:多进程编程
# @time: 2023/3/2  19:58
# import time
# from multiprocessing import Process
#
#
# def pname(name):
#     print(f'{name} hhhh')
#     time.sleep(5)
#     print(f"{name} hhahhha")
#
#
# if __name__ == '__main__':
#     p = Process(target=pname, args=("name",))
#     p.start()  # 子进程开始
#     print("主进程结束")


# 方法2  面向对象的方式
# from multiprocessing import Process
# import time
#
#
# # 继承Process类
# class MyProcess(Process):
#     def run(self):
#         print("任务开始")
#         time.sleep(5)
#         print("任务结束")
#
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()
#     print("主程序结束")


import time
from multiprocessing import Process, current_process
import os


# 打印当前进程号
def process():
    # multiprocessing提供的
    print(f"第{current_process().pid}执行中")
    # os模块提供的
    print(f"第{os.getpid()}执行中")
    time.sleep(100)


if __name__ == '__main__':
    p = Process(target=process)
    p.start()
    print("主进程结束！")
