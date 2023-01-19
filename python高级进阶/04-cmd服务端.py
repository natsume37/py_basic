# coding : utf-8
# 夏目&青一
# @name:cmd服务端
# @time: 2023/1/19  15:50
import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8081))
server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
        except:
            break
        if not cmd:
            break

        # 执行终端命令
        obj = subprocess.Popen(cmd.decode('utf-8'),
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                               )
        out_res = obj.stdout.read()
        err_res = obj.stderr.read()

        data_size = len(out_res) + len(err_res)
        # conn.send(str(data_size).encode('utf-8'))  # 头部（固定头部数据）
        header = bytes(str(data_size).encode('utf-8')).zfill(8)
        print(header)
        conn.send(header)
        conn.send(out_res)
        conn.send(err_res)


    conn.close()
