import requests
import time
from openpyxl import Workbook


def get_data():
    data = []  # 用来保存爬取到的数据
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'referer': 'http://movie.mtime.com/'
    }

    # 以 50 条为一页，共 4 页
    for num in range(1, 5):
        params = {
            "tt": "{}".format(int(time.time() * 1000)),
            # 电影id：209164
            "movieId": "209164",
            "pageIndex": "{}".format(num),
            "pageSize": "50",
            # 按最新评论排序
            "orderType": "2"
        }

        res = requests.get(
            'http://front-gateway.mtime.com/library/movie/comment.api',
            params=params,
            headers=headers
        )

        comment_list = res.json()['data']['list']
        for comment in comment_list:
            row = [comment['nickname'], comment['content'], comment['rating']]
            data.append(row)
        # 暂停一下，防止爬取太快被封
        time.sleep(1)

    # 返回爬取到的内容
    return data


def save_data(data):
    # 创建工作簿并选中当前工作表
    wb = Workbook()
    sheet = wb.active
    sheet.title = '评论数据'
    # 写入表头
    header = ['用户昵称', '影评内容', '用户打分']
    sheet.append(header)
    # 写入数据
    for row in data:
        sheet.append(row)
    # 保存工作簿
    wb.save('西游记之大圣归来.xlsx')


save_data(get_data())