# coding : utf-8
# 夏目&青一
# @name:matb数据可视化
# @time: 2023/1/29  19:04


import matplotlib.pyplot as plt

# # 日本料理
# x = ['味增汤', '寿司', '手握拳', '炸虾', '生鱼片', '天妇罗']
# # 价格
# y = [35, 60, 83, 100, 139, 67]
# # 设置字体，解决中文乱码问题
# plt.rcParams['font.family'] = ['Noto Sans CJK JP']
# plt.plot(x, y, 'bo--')
# plt.show()

# 折线图

# 日本料理
# x = ['味增汤', '寿司', '手握拳', '炸虾', '生鱼片', '天妇罗']
# # 价格
# y = [35, 60, 83, 100, 139, 67]
# # 设置字体，解决中文乱码问题
# plt.rcParams['font.family'] = ['SimHei']  # SimHei（黑体）
# plt.plot(x, y, '-')
# plt.show()

# 显示图例
# x = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# y1 = [61, 42, 52, 72, 86, 91, 73]
# y2 = [23, 26, 67, 38, 46, 55, 33]
# plt.rcParams['font.family'] = ['SimHei']  # SimHei（黑体）
# # 传入 label 参数
# plt.plot(x, y1, label='商品 A')
# plt.plot(x, y2, label='商品 B')
# # 显示图例
# plt.legend(loc='lower right') # 设置图例的位置（11种）
# plt.xlabel('时间')
# plt.ylabel('销量')
# plt.show()

# 小测试
import numpy as np

dates = [
    '01月', '02月', '03月', '04月', '05月', '06月',
    '07月', '08月', '09月', '10月', '11月', '12月'
]
values = np.genfromtxt('./values/收盘价.csv', delimiter=',')
v_baidu = values[:, 0]
v_tx = values[:, 1]
v_ali = values[:, 2]
plt.rcParams['font.family'] = ['SimHei']
plt.plot(dates, v_baidu, label = '百度')
plt.plot(dates, v_tx, label = '腾讯')
plt.plot(dates, v_ali, label = '阿里')
plt.xlabel('日期')
plt.ylabel('销量')
plt.show()
