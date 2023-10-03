"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : NumPy.py
@Author : 夏目&青一
@Time : 2022/12/15 22:44

"""
# 数组是一系列--相同类型--数据的集合
# 创建一个多维数组   array()创建多维数组
import numpy as np
import pandas

# data = np.array([1, 2, 3])
# print(data)  # [1 2 3]
# print(type(data))  # <class 'numpy.ndarray'>
#
#
# # np.ones(),np.zeros()  传入参数，生成1个或0个多维数组  默认生成的是浮点数
# ones = np.ones(3)
# print(ones)     # [1. 1. 1.]  默认生成的是浮点数，np会省略小数点后的0
#
# zeros = np.zeros(3, dtype='int')   # 指定生成int类型的数组
# print(zeros)  # [0. 0. 0.]


# 多维数组间的四则运算 两数组对应位置进行运算
# data = np.array([1, 2, 3])
# ones = np.ones(3)
# print(data + ones)  # [2. 3. 4.]
# pass

# 多维数组和常数运算  Broadcasting 现象（大范围传播、投射---！广播）
# 因为 Broadcasting 规则，[1 2] + 1 相当于 [1 2] + [1 1]，因此结果为 [2 3]。

# print(data + 1)  # [2 3 4]

# 练习1
# 将下面的数组 [1 2 3] 经过运算得到数组 [2. 2. 2.] 并打印出来
# data = np.array([1, 2, 3])
# print(data * 2 / data)


# 索引：numpy 中多维数组的索引也是从 0 开始，以多维数组的长度减 1 结束。写法也和列表索引一样：
# data = np.array([1, 2, 3])
# print(data[0])  # 1

# 反向索引 用 data[-1] 获取数组中的最后一个元素
# print(data[:-1])  # [1 2]

# 分片 ：data[m:n]。分片是左闭右开区间，即包含 m 不包含 n
# print(data[:2])  # [1 2]

# 对列表分片后的数据进行更改不会影响原数据，但对多维数组分片后的数据进行更改会影响到原数据
# 列表
# lst_data = [1, 2, 3]
# lst_data2 = lst_data[:]
# lst_data2[0] = 6
# print(lst_data)
# 输出：[1, 2, 3]

# 多维数组
# arr_data = np.array([1, 2, 3])
# arr_data2 = arr_data[:]
# arr_data2[0] = 6
# print(arr_data)
# 输出：[6 2 3]

# 如需真的要备份  arr_data[:].copy()
# 步长 设置
# data = np.array([1, 2, 3, 4, 5, 6])
# print(data[::2])  # 省略前两个参数
# 输出：[1 3 5]

# 当步长为负数时，会将顺序反转。我们可以利用这个特性来实现列表或多维数组的快速反转
# data = np.array([1, 2, 3, 4, 5, 6])
# print(data[::-1])  # [6 5 4 3 2 1]


# 通用方法：
# 在介绍通用方法前，我先向你提个问题：假设你是某篮球俱乐部的教练，现在首发阵容还差一人。现有三名球员备选，
# 他们近 10 场比赛的得分数据如下，你会选择谁进入首发阵容呢？
# player1 = np.array([7, 9, 10, 9, 11, 13, 10, 10, 11, 10])
# player2 = np.array([7, 9, 8, 9, 11, 10, 11, 12, 10, 13])
# player3 = np.array([3, 7, 10, 3, 6, 30, 10, 7, 11, 13])

# mean()求多维数组中所有数据的平均值
# print('一号球员十场比赛的平均值为', player1.mean())  # 一号球员十场比赛的平均值为 10.0
# print('二号球员十场比赛的平均值为', player2.mean())  # 二号球员十场比赛的平均值为 10.0
# print('三号球员十场比赛的平均值为', player3.mean())  # 三号球员十场比赛的平均值为 10.0

# 方法2

# print('球员1得分的平均数为', player1.mean())
# print('球员2得分的平均数为', player2.mean())
# print('球员3得分的平均数为', player3.mean())
# print('====================')
# print('球员1得分的中位数为', np.median(player1))
# print('球员2得分的中位数为', np.median(player2))
# print('球员3得分的中位数为', np.median(player3))
# print('====================')
# print('球员1得分的标准差为', player1.std())
# print('球员2得分的标准差为', player2.std())
# print('球员3得分的标准差为', player3.std())

# 球员1得分的平均数为 10.0
# 球员2得分的平均数为 10.0
# 球员3得分的平均数为 10.0
# ====================
# 球员1得分的中位数为 10.0
# 球员2得分的中位数为 10.0
# 球员3得分的中位数为 8.5
# ====================
# 球员1得分的标准差为 1.4832396974191326
# 球员2得分的标准差为 1.7320508075688772
# 球员3得分的标准差为 7.362064927722384


# 需要注意的是，求中位数的 median() 方法只有 numpy 上有，只能使用 np.median(data) 来求中位数
#  numpy常用函数
"""
mean()  求平均数
median()    求中位数
min()   求最小数
max()   最大数
ptp()   求极差
std()   求标准差
var()   求方差
"""

# 二维数组
# 单层嵌套列表
# nested_list = [[1, 2], [3, 4]]
# print(nested_list)
# 输出：[[1, 2], [3, 4]]

# 二维数组
# data = np.array(nested_list)
# print(data)
# 输出：
# [[1 2]
#  [3 4]]

# ones() 和 zeros() 方法同样也能快速创建元素全为 1 和 0 的二维数组
# ones = np.ones((3, 2))
# print(ones)
# 输出：
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]
# print('分页'.center(20, '-'))
# zeros = np.zeros((3, 2))
# print(zeros)
# 输出：
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]

# 接下来我们来认识几个描述多维数组的属性：
#
# ndim：多维数组维度的个数。例如：二维数组的 ndim 为 2；
# shape：多维数组的形状。它是一个元组，每个元素分别表示每个维度中数组的长度。对于 m 行和 n 列的的数组，它的 shape 将是 (m, n)。因此，shape 元组的长度（元素个数）就是 ndim 的值；
# size：多维数组中所有元素的个数。shape 元组中每个元素的乘积就是 size 的值；
# dtype：多维数组中元素的类型。
# data = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(f"ndim", data.ndim)
# 输出：
# ndim: 2
# shape: (2, 3)
# size: 6
# dtype: int64


# axis 轴
# 布尔索引
# data  = np.array([[1, 2, 3], [4, 5, 6]])
# print(data > 3)

# [[False False False]
#  [ True  True  True]]

# &运算
# data = np.array([[1, 2], [3, 4], [5, 6]])
# print(data[(data > 3) & (data < 5)])
# 输出：[4]

# 区别在于：and 改用 &，or 改用 |，not 改用 ~，并且每个条件要用括号括起来！！！


# data = np.array([[1, 2], [3, 4], [5, 6]])
# 大于 3 或者小于 2
# print(data[(data > 3) | (data < 2)])
# 输出：[1 4 5 6]

# 大于 3 或者不小于 2（即大于等于 2）
# print(data[(data > 3) | ~(data < 2)])
# 输出：[2 3 4 5 6]

# 除此之外，我们还能使用 == 和 != 来进行数据的筛选、、

# data = np.array([[1, 2], [3, 4], [5, 6]])
# # 等于 3
# print(data[data == 3])
# # 输出：[3]
#
# # 不等于 3
# print(data[data != 3])
# 输出：[1 2 4 5 6]

# arange()
# data = np.arange(1,10)
# print(data)
# # [1 2 3 4 5 6 7 8 9]

# np.random.rand()  np.random.randint()  # np.random.randint(m, n) 生成的是 [m, n) 之间的整数，这点一定注意要区分。
# data = np.random.rand(2, 3)  # 方法可以生成多个 [0, 1) 之间的随机小数，只需我们传入要生成的随机数组的形状（shape）即可
# print(data)
# [[0.79201151 0.27942238 0.803801  ]
#  [0.31979502 0.30996317 0.0635928 ]]
