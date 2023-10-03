# coding : utf-8
# 夏目&青一
# @name:03_lock
# @time: 2023/2/4  15:05
import threading
import time

a = 0


def work():
    time.sleep(1)
    global a
    for i in range(100000):
        a += 1


thread_list = []
for i in range(5):
    t = threading.Thread(target=work)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print(a)

# 概率问题，bug难以复现
