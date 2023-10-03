# coding : utf-8
# 夏目&青一
# @name:
# @time: 2023/1/19  14:18

import socketserver
import time



class RequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)  # self.request => 元组
        print(self.client_address)
        self.request[1].sendto(self.request[0].upper(), self.client_address)


sk = socketserver.ThreadingUDPServer(('127.0.0.1', 5000), RequestHandle)
sk.serve_forever()

# 1、创建socket对象
