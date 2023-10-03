# coding : utf-8
# 夏目&青一
# @name:linux_txun
# @time: 2023/2/28  17:35
import json
import socketserver
import time

list_session = [
    {
        "user": "系统提示",
        "usr_img": "欢迎来到聊天室",
    }
]


class RequestHandle(socketserver.BaseRequestHandler):
    global list_session
    time.sleep(1)

    def handle(self) -> None:
        print(self.request)  # self.request => conn
        print(self.client_address)
        # 5、数据传输
        while True:
            # winds解决断开问题
            try:
                header_json = json.dumps(list_session)
                header_bytes = header_json.encode('utf-8')
                header_h = bytes(str(len(header_json)), 'utf-8').zfill(4)

                # 完整数据
                self.request.send(header_h)
                self.request.send(header_bytes)
            except:
                break

        # mac\linux系统解决退出问题

            data = self.request.recv(4)
            if not data:
                break
            data = data.decode('utf-8')
            mgs_h = int(data)
            mgs = self.request.recv(mgs_h)
            mgs = mgs.decode('utf-8')
            res = json.loads(mgs)
            list_session.append(res)


        # 6、结束服务
        self.request.close()

sk = socketserver.ThreadingTCPServer(('127.0.0.1', 8098), RequestHandle)
print('服务器启动成功')
sk.serve_forever()
print(list_session)
print("服务器已关闭！！")
