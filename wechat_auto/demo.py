import json
import time
from uiautomation import WindowControl, SendKeys
import requests


def chat_auto(mag):
    headers = {
        'Api-Key': 'bshpbitz47txrw7y',
        'Api-Secret': 'igz9b9dp',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    payload = {
        "content": f"{mag}",
        "type": 1,
        "from": "黄蕊",
    }

    res = requests.post('https://api.mlyai.com/reply', headers=headers, json=payload)
    return res.json()['data'][0]['content']


def read_unread_messages():
    # 绑定微信主窗口
    wx = WindowControl(Name='微信', searchDepth=1)
    wx.ListControl()
    wx.SwitchToThisWindow()

    # 寻找会话控件绑定
    hw = wx.ListControl(Name='会话')

    # 死循环获取未读信息
    while True:
        # 从查找未读消息
        unread_contacts = hw.TextControl(searchDepth=4)

        # 死循环维持，没有超时报错
        while not unread_contacts.Exists():
            # time.sleep(0.1)  # 等待0.1秒
            unread_contacts = hw.TextControl(searchDepth=4)

        # 存在未读消息
        if unread_contacts.Name:
            # 点击未读消息
            unread_contacts.Click(simulateMove=False)

            # 读取最后一条消息
            last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name

            print("未读消息:", last_msg)

            # 处理未读消息，这里可以根据需求进行进一步处理
            to_chat = chat_auto(last_msg)
            SendKeys(to_chat, waitTime=1)
            SendKeys('{Enter}', waitTime=1)

            # 退回主页
            wx.SendKeys('{Ctrl}r', waitTime=1)

        # 等待
        time.sleep(0.1)


if __name__ == "__main__":
    read_unread_messages()
