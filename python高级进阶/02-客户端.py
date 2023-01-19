# coding : utf-8
# 夏目&青一
# @name:02-客户端
# @time: 2023/1/19  14:18

import socket
# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 流式协议（tcp协议）

# 2、开始建立链接
sk.connect(('127.0.0.1', 5000))

# 3、传输数据
while True:
    msg = input('请输入>>>').strip()
    if not msg:
        continue
    sk.send(msg.encode('utf-8'))
    if msg == 'q' or msg == 'Q':
        break

    data = sk.recv(1024)
    print(data.decode('utf-8'))

# 4、关闭链接
sk.close()