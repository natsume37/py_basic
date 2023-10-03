# coding : utf-8
# 夏目&青一
# @name:Queue模块
# @time: 2023/3/3  15:55

# from multiprocessing import Queue
#
# # 定义最大队列数，默认为3000多
# q = Queue(6)
#
# q.put("a")
# q.put("b")
# q.put("c")
# q.put("d")
# q.put("e")
# q.put("f")
#
# # 放数据不等待、队列已满就报错
# # q.put_nowait("g")
#
# # 设置超时时间  数据已满、三秒后数据还是满的就报错
# # q.put("g", timeout=3)
#
#
# # 报错信息：queue.Full
# v1 = q.get()
# v2 = q.get()
# v3 = q.get()
# v4 = q.get()
# v5 = q.get()
# v6 = q.get()
#
# # 如果数据为空、则等待 （默认）
# # get 解决等待 解除等待
# # v7 = q.get_nowait()
# # v7 = q.get(timeout=3)
#
# # print(q.full()) 判断数据是否已满
# # print(q.empty()) 判断队列是否为空
# print(v1, v2, v3)
# # a b c


from multiprocessing import Process, Queue


def tesk1(q):
    q.put("宫保鸡丁")


def tesk2(q):
    # 注意：这里并不需要等待子进程、因为：q.get()有等待！！
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=tesk1, args=(q,))
    p2 = Process(target=tesk2, args=(q,))

    p1.start()
    p2.start()
