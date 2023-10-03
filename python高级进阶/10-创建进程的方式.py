# coding : utf-8
# 夏目&青一
# @name:10-创建进程的方式
# @time: 2023/5/12  14:17

from multiprocessing import Process
import time

# def func(name):
#     print(f"{name}进程开始")
#     time.sleep(5)
#     print(f"{name}进程结束")
# if __name__ == '__main__':
#     p = Process(target=func, args=("小明",))
#     p.start()
#     print("主进程结束")
# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.task_name = name
#
#     def run(self) -> None:
#         print(f"{self.task_name}任务开始")
#         time.sleep(3)
#         print(f"{self.task_name}进程结束")
#
#
# if __name__ == '__main__':
#     p = MyProcess('哈哈哈')
#     p.start()
#     print("主进程结束")

# from multiprocessing import Process, current_process
# import os
# def func():
#     print(f'进程号为：{current_process().pid}')
#     print(os.getpid())
#     time.sleep(10)
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     p.terminate() # s杀死进程号
#
#
#     print(f"主进程号为：{current_process().pid}")
#     print(os.getpid())


from multiprocessing import Process
import time


def task(name):
    print(f'{name} 活着')
    time.sleep(3)
    print(f'{name} 死了')


if __name__ == '__main__':
    p = Process(target=task, args=('妲己',))
    p.daemon = True
    p.start()
    time.sleep(1)
    print("纣王死了,妲己也要死")
    print('全部结束')
