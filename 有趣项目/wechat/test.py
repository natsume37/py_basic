# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: test
# @TIME: 2023/11/10 20:54
import time

token = '74_0F316jGix3nDWdGZ4KNQPIBVAQuPfxGeoSvGg0FJE-GRaTjAhMpyKZ-BxWVIgs6JJIne2OwroYybw83ydUvmbpXGVMxMzGb1ItpOGwDp5i7zAq2dWxLk2zlvtuwLXJhADAGSE'

from flask import Flask, request, make_response
import hashlib

app = Flask(__name__)

# 设置你的微信 Token
WECHAT_TOKEN = "token"


@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # 验证签名
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')

        # 排序并加密
        token = WECHAT_TOKEN
        data = [token, timestamp, nonce]
        data.sort()
        sha1 = hashlib.sha1()
        sha1.update(''.join(data).encode('utf-8'))
        hashcode = sha1.hexdigest()

        # 对比签名
        if hashcode == signature:
            return echostr
        else:
            return "Verification failed."

    if request.method == 'POST':
        # 处理消息
        from_xml = request.data
        # 在这里解析消息，判断消息类型，然后回复 "hello"
        response = """
        <xml>
            <ToUserName><![CDATA[{0}]]></ToUserName>
            <FromUserName><![CDATA[{1}]]></FromUserName>
            <CreateTime>{2}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[hello]]></Content>
        </xml>
        """.format(request.form['FromUserName'], request.form['ToUserName'], int(time.time()))
        return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
