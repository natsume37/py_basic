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

    data_size = int(client.recv(8).decode('utf-8'))
    recv_size = 0
    data = b''
    while recv_size < data_size:
        res = client.recv(1024)
        recv_size += len(res)
        data += res
    print(data.decode('utf-8'))
    print(len(data))



