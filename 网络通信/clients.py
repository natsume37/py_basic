# coding : utf-8
# 夏目&青一
# @name:02-客户端
# @time: 2023/1/19  14:18
import json
import queue
import socket
from multiprocessing import Process
from  queue import Queue
# 线程安全问题
# 1、创建socket对象
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 流式协议（tcp协议）

# 2、开始建立链接  124.222.68.76 , 127.0.0.1
sk.connect(('127.0.0.1', 8098))
name = input('请输入你的昵称>>> ').strip()


# 3、传输数据
def recv():
    while True:
        time.sleep(1)
        data = sk.recv(4)
        data = data.decode('utf-8')
        mgs_h = int(data)

        mgs = sk.recv(mgs_h)
        mgs = mgs.decode('utf-8')
        res = json.loads(mgs)
        for i in res:
            name = i["user"]
            msgs = i["usr_img"]
            print(f"\033[37m{name}:  \033[31m{msgs}\033[0m")
        print()

def send():
    while True:
        msg = input('请输入发送文本：').strip()
        if not msg:
            continue

        if msg == 'q' or msg == 'Q':
            break
        header = {
            'user': name,
            'usr_img': msg,
        }
        header_json = json.dumps(header)
        header_bytes = header_json.encode('utf-8')
        header_h = bytes(str(len(header_json)), 'utf-8').zfill(4)
        sk.send(header_h)
        sk.send(header_bytes)



if __name__ == '__main__':
    p = [
        Process(target=recv),
        Process(target=send)
    ]
    q = Queue.get()
    for i in p:
        i.start()

    for i in p:
        i.join()

# 4、关闭链接
    sk.close()
