# coding : utf-8
# 夏目&青一
# @name:
# @time: 2023/1/19  14:18

import socket
# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 数据报协议（udp协议）

# 2、绑定地址
sk.bind(('127.0.0.1', 5000))


# 5、数据传输
while True:
    # winds解决断开问题
    data, addr = sk.recvfrom(1024)
    print(f'{addr}发过来的数据：', data)
    sk.sendto(data.upper(), addr)

