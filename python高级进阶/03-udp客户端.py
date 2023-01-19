# coding : utf-8
# 夏目&青一
# @name:
# @time: 2023/1/19  14:18

import socket

# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 数据报协议（udp协议）

# 3、传输数据
while True:
    msg = input('请输入>>>').strip()
    sk.sendto(msg.encode('utf-8'), ('127.0.0.1', 5000))

    data, addr = sk.recvfrom(1024)
    print(data)



# 4、关闭链接
sk.close()
