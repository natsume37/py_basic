# coding : utf-8
# 夏目&青一
# @name:04-cmd客户端
# @time: 2023/1/19  15:50
import os
import socket
import json



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.25.215', 5001))
while True:
    cmd = input('请输入终端命令>>>').lower().strip()
    if not cmd:
        continue
    if cmd == 'q':
        break

    # 发送命令到云端
    cmd_h = bytes(str(len(cmd.encode('utf-8'))), 'utf-8')
    client.send(cmd_h)
    client.send(cmd.encode('utf-8'))

    order = cmd.split()
    order_header = order[0]

    # get请求
    if order_header == 'get':
        file_name = order[1]
        print(file_name)
        # 接收数据头长和头
        header_hby = client.recv(4)  # 头部多长
        header_h = header_hby.decode('utf-8')
        header_tag = client.recv(int(header_h))

        # 处理头
        header_res = json.loads(header_tag)

        file_size = header_res['file_size']
        # 正式接收header_tag
        print('开始接收文件：', header_res['file_name'])
        recv_size = 0
        print('file_size', header_res['file_size'])
        while recv_size < header_res['file_size']:
            tag = client.recv(1024)
            recv_size += len(tag)
            with open(rf'C:\Users\19570\Desktop\{file_name}', 'a+b') as f:
                f.write(tag)
        print('传输完成')
        print(f"文件大小为：{header_res['file_size']}")
        client.send('接收成功！'.encode('utf-8'))

    # post请求
    elif order_header == 'post':
        file_name = order[1]
        print(file_name)
        header = {
            'file_name': file_name,
            'file_size': os.path.getsize(file_name),
            'md5': '测试简化！'
        }
        # 发送头长和头文件
        header_bytes = json.dumps(header).encode('utf-8')
        header_h = bytes(str(len(header_bytes)), 'utf-8').zfill(4)

        client.send(header_h)
        client.send(header_bytes)

        res = 0
        # 开始发送数据
        while res < header['file_size']:
            with open(file_name, 'rb')as f:
                data = f.read(1024)
                client.send(data)
                res = len(data)

        print(res)
        print('发送结束')

    # cmd
    else:
        # 接收云端返回结果
        header_size = client.recv(8)
        recv_size = 0
        data = b''
        while recv_size < int(header_size.decode('utf-8')):
            res = client.recv(1024)
            data += res
            recv_size += len(res)
        print(data.decode('utf-8'))
        print(int(header_size.decode('utf-8')))

client.close()
