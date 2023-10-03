# coding : utf-8
# 夏目&青一
# @name:同步_异步
# @time: 2023/2/17  20:49

from multiprocessing import Process
import time


def func(name):
    print(f'{name}任务开始')
    time.sleep(5)
    print(f'{name}任务结束')


# 1、调用类、得到一个进程操作对象
p = Process(target=func, args=('进程',))

# winds解决方法：win会把这个文件全部导入，产生无限循环递归
if __name__ == '__main__':
    # 2、创建进程！！！
    p.start()
    print('主进程结束')
