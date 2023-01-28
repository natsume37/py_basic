# coding : utf-8
# 夏目&青一
# @name:cmd服务端
# @time: 2023/1/19  15:50
import json
import socket  # 套接字
import subprocess
import os
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8089))
server.listen(5)
print('服务器已启动！')

while True:
    conn, addr = server.accept()
    print(addr, datetime.now())
    while True:
        try:
            cmd_h = conn.recv(4)
        except:
            break
        if not cmd_h:
            break
        cmd_h = cmd_h.decode('utf-8')
        cmd = conn.recv(int(cmd_h))
        print(f'order:', cmd.decode('utf-8'), datetime.now())
        cmd_file = cmd.decode('utf-8').split()

        # get 请求
        if cmd_file[0] == 'get':
            tag_name = cmd_file[1]
            tag_size = os.path.getsize('E:\py_project\python高级进阶\文件存放\哈哈哈哈.txt')

            # 添加文件头
            # 发放自定义文件头
            header = {
                'file_name': tag_name,
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

        # post请求
        elif cmd_file[0] == 'post':
            post_name = cmd_file[1]

            # 接收头文件
            post_h = conn.recv(4).decode('utf-8')
            post_header = conn.recv(int(post_h))

            header = json.loads(post_header.decode('utf-8'))
            file_name = header['file_name']


            # 文件名切割：
            file_name, = file_name.split('\\')[-1:]
            save_size = 0
            print(f'文件{file_name}传输中...')
            while save_size < header['file_size']:
                with open(f'./文件存放/{file_name}', 'a+b')as f:
                    res = conn.recv(1024)
                    save = f.write(res)
                    save_size += len(res)
            print(save_size)
            print('接收完毕')


        # 执行终端命令
        else:
            obj = subprocess.Popen(cmd.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
            out_res = obj.stdout.read()
            err_res = obj.stderr.read()

            res_size = str(len(out_res) + len(err_res))
            conn.send(res_size.encode('utf-8').zfill(8))
            conn.send(out_res)
            conn.send(err_res)
    conn.close()
