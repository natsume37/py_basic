# coding : utf-8
# 夏目&青一
# @name:02-服务端
# @time: 2023/1/19  14:18
import socketserver
import socket


class RequestHandle(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        # print(self.request)   # self.request => conn
        print(self.client_address)
        # 5、数据传输
        while True:
            # winds解决断开问题
            try:
                data = self.request.recv(1024)
            except:
                break
            # mac\linux系统解决退出问题
            if not data:
                break
            data = data.decode('utf-8')
            print('客户端发过来的数据：', data)
            self.request.send(data.upper().encode('utf-8'))

        # 6、结束服务
        self.request.close()


sk = socketserver.ThreadingTCPServer(('127.0.0.1', 5001), RequestHandle)
sk.serve_forever()
# 等价于
# while True:
#     conn, addr = sk.accept()
#     起一个线程（conn, addr）






