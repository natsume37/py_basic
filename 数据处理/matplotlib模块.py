# coding : utf-8
# 夏目&青一
# @name:matplotlib模块
# @time: 2023/1/29  16:30

# matplotlib比较庞大，用其中一个子模块
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 2 * np.pi, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, x, y2)
# plt.show()  # 这行代码不能丢，否则不显示图像

# x = np.arange(0, 2 * np.pi, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, 'ro--')  # 正弦函数图像
# plt.plot(x, y2, 'b*-.')  # 余弦函数图像
# # 等价于 plt.plot(x, y1, 'ro--', x, y2, 'b*-.')
# plt.show()

# 老师礼物

t = np.arange(-6, 6, 0.1)
x = 16* np.power(np.sin(t), 3)
y = 13 * np.cos(t) - 5* np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
plt.plot(x, y, 'r')
plt.show()