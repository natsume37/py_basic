# coding : utf-8
# 夏目&青一
# @name:06-文件客户端
# @time: 2023/1/27  16:57
import json
import socket
import os

# 1、创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 流式协议（tcp协议）

# 2、开始建立链接
client.connect(('124.22.68.76', 5001))

# 3、传输数据
while True:
    msg = input('请输入命令>>>').lower().strip()
    if not msg:
        continue
    mag_h = bytes(str(len(msg.encode('utf-8'))), 'utf-8').zfill(4)
    client.send(mag_h)
    client.send(msg.encode('utf-8'))
    if msg == 'q':
        break

    order, file_path = msg.split()
    print(order, file_path)
    if order == 'get':
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
            with open(rf'C:\Users\19570\Desktop/{file_path}', 'ab') as f:
                f.write(tag)
        print('传输完成')
        print(f"文件大小为：{header_res['file_size']}")
        client.send('接收成功！'.encode('utf-8'))
    # post 上传请求
    elif order == 'post':
        # try:
        true_msg = client.recv(4)
        file_size = os.path.getsize(file_path)
        header = {
            'file_name': file_path,
            'file_size': file_size
        }
        header_json = json.dumps(header)
        header_bytes = bytes(str(header_json), 'utf-8').zfill(4)
        client.send(header_bytes)
        send_size = 0
        while send_size < file_size:
            with open(file_path, 'wb') as f:
                client.send(f.read(1024))

    # except:
    #     print('上传失败！')

# 4、关闭链接
client.close()
