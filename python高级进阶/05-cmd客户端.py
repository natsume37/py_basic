# coding : utf-8
# 夏目&青一
# @name:04-cmd客户端
# @time: 2023/1/19  15:50

import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8081))
while True:
    cmd = input('请输入终端命令>>>').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # 粘包问题解决

    # 拿到固定的头部长度
    header_size = int(client.recv(4).decode('utf-8'))
    header_json = client.recv(header_size).decode('utf-8')
    header = json.loads(header_json)
    print(header)

    data_size = header['file_size']
    print(data_size)
    recv_size = 0
    data = b''
    while recv_size < data_size:
        res = client.recv(1024)
        recv_size += len(res)
        data += res
    print(data.decode('utf-8'))
    print(len(data))
