# coding : utf-8
# 夏目&青一
# @name:02-服务端
# @time: 2023/1/19  14:18

import socket
# 1、创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 流式协议（tcp协议）

# 2、绑定地址
sk.bind(('0.0.0.0', 5001))

# 3、监听链接请求（开始营业）
sk.listen(5)  # 半连接池大小、等待区
print('服务端启动成功，在5001端口等待客户端链接')

# 4、取出半连接池的链接请求，开始服务

# 持续提供服务、并发提供服务
while True:
    conn, addr = sk.accept()
    print('链接对象：', conn)
    print('客户端ip+端口：', addr)

    # 5、数据传输
    while True:
        # winds解决断开问题
        try:
            data = conn.recv(1024)
        except:
            break
        # mac\linux系统解决退出问题
        if not data:
            break
        data = data.decode('utf-8')
        print('客户端发过来的数据：', data)
        conn.send(data.upper().encode('utf-8'))

    # 6、结束服务
    conn.close()

