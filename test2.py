# from multiprocessing import Queue, Process, JoinableQueue
# import time
# import random
#
#
# def producer(name, food, q):
#     for i in range(8):
#         time.sleep(random.randint(2, 4))
#         q.put(food)
#         print(f"{name} 做了{food}{i}")
#
#
# def consumer(name, q):
#     while True:
#         v = q.get()
#         time.sleep(random.randint(1, 3))
#         print(f"{name} 吃了{v}")
#
#         q.task_done()  # 告诉队列、我们已经拿走了一个数据、并且已经处理完了
#
#
# '''
# JoinableQueue
# 在Queue的基础上多了一个计数器机制，每put一个数据，计数器就加一
# 每调用一次task_done,计数器就减
# 当计数器为0的时候，就会走q.join后面的代码
# '''
#
# if __name__ == '__main__':
#     q = JoinableQueue()
#     p1 = Process(target=producer, args=("小当家", "黄金炒饭", q))
#     p2 = Process(target=producer, args=("神厨小福贵", "佛跳墙", q))
#     c1 = Process(target=consumer, args=("八戒", q))
#
#     c1.daemon = True  # 设置守护进程、主进程死后、子进程也要死、而不是等待。
#
#     p1.start()
#     p2.start()
#     c1.start()
#
#     p1.join()  # 必须加
#     p2.join()  # 必须加（保证每个数据全部处理完）
#
#     q.join()
#     print("主程序执行完毕")
#     # 主进程死了、子进程也要陪葬。（设置守护进程）


# 填充API Key与Secret Key


import requests
import json


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=[应用API Key]&client_secret=[应用Secret Key]"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "给我推荐一些自驾游路线"
            }
        ],
        "stream": True
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, stream=True)

    for line in response.iter_lines():
        print(line)


if __name__ == '__main__':
    main()
