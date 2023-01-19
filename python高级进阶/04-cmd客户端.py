# coding : utf-8
# 夏目&青一
# @name:04-cmd客户端
# @time: 2023/1/19  15:50

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8081))
while True:
    cmd = input('请输入终端命令>>>').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # 粘包问题解决
    # 拿到数据总长度

    header = client.recv(8)
    # print(res.decode('utf-8'))
    res = client.recv(int(header))
    print(res.decode('utf-8'))

