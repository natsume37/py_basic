# coding : utf-8
# 夏目&青一
# @name:06-文件服务端
# @time: 2023/1/27  16:56
import socket
import os
import json
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5001))

server.listen(5)
print('服务器启动成功！')

while True:
    conn, addr = server.accept()
    print(conn)
    while True:
        try:
            data = conn.recv(4)
        except:
            break
        if not data:
            break

        data_header, tag_name = data.decode('utf-8').split()
        if data_header == 'get':
            try:
                print(data_header)
                tag_size = os.path.getsize(r'\root\work')

                # 添加文件头
                # 发放自定义文件头
                header = {
                    'file_name': '哈哈哈哈.txt',
                    'file_size': tag_size,
                    'md5': 'dsaflasdcdsvdsf'
                }
                # 发送文件头
                header_json = json.dumps(header)
                header_bytes = header_json.encode('utf-8')
                header_h = bytes(str(len(header_bytes)), 'utf-8').zfill(4)

                conn.send(header_h)
                conn.send(header_bytes)

                print('发送数据头成功')

                data_size = 0
                with open(f'./文件存放/{tag_name}', 'rb') as f:
                    # 文件tag
                    while data_size < tag_size:
                        data = f.read(1024)
                        conn.send(data)
                        data_size += len(data)
                print('发送完成')

                res = conn.recv(1024)
                res = res.decode('utf-8')
                print(res)
            except:
                print('请输入正确的命令')
        elif data_header == 'post':
            conn.send('准备接收'.encode('utf-8').zfill(4))
            post_header = conn.recv(4)
            print(post_header.decode('utf-8'))
            # 解析post_header
            post_header = json.loads(post_header)
            header = post_header.decode('utf-8')
            file_name = header['file_name']
            file_name[:-1] = file_name.split('\\')
            file_size = header['file_size']
            recv_size = 0
            while recv_size < file_size:
                file_bytes = conn.recv(1024)
                with open(file_name, 'a+b')as f:
                    f.write(file_bytes)
            print(f'文件{file_name}传输完毕！')

    server.close()
