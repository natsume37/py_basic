# coding : utf-8
# 夏目&青一
# @name:06-文件客户端
# @time: 2023/1/27  16:57
import json
import socket

# 1、创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 流式协议（tcp协议）

# 2、开始建立链接
client.connect(('127.0.0.1', 8090))

# 3、传输数据
while True:
    msg = input('请输入命令>>>').lower().strip()
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    if msg == 'q':
        break
    order, file_name = msg.split()
    # 接收数据头
    header_hig = client.recv(4)  # 头部多长
    header_h = header_hig.decode('utf-8')

    # 正式接收header_tag
    header_res = client.recv(int(header_h))
    header_res = header_res.decode('utf-8')
    print(header_res)

    header_res = json.loads(header_res)
    print('文件名：', header_res['file_name'])
    size = 0
    print('file_size', header_res['file_size'])
    while size < header_res['file_size']:
        tag = client.recv(1024)
        size += len(tag)
        with open(rf'C:\Users\19570\Desktop/{file_name}', 'ab') as f:
            f.write(tag)
    print('传输完成')
    print(f"文件大小为：{header_res['file_size']}")
    client.send('接收成功！'.encode('utf-8'))

# 4、关闭链接
client.close()
