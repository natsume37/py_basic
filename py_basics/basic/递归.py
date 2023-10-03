"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 递归.py
@Author : 夏目&青一
@Time : 2022/12/11 12:10

"""

# 递归  (直接引用，间接引用)
# 在调用一个函数的过程中，有调用了自己本身这个函数    默认 1000层
# import sys
#
# print(sys.getrecursionlimit())   # 查看最高递归层数
# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())
#
# def func():
#     print('夏目')
#     func()
#
# # func()

# 递归调用的应用
# num = 100
#
#
# def ad(x):
#     if x == 0:
#         return 0
#     return x + ad(x - 1)
#
#
# count = ad(num)
# print(count)

# 应用
# 一、要求：把下面列表的每一个值单独答应出来
# l = [1, 2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12]]]]]]]]]]]
#
#
# def func(li):
#     for i in li:
#         if type(i) is list:
#             func(i)
#         else:
#             print(i)
#
# func(l)
# 二、把下列的字符串做全排列
# s = 'abc'
# l = list(s)
#
#
# def permutation(l, level):
#     if level == len(l):
#         print(l)
#     for i in range(level, len(l)):
#         l[level], l[i] = l[i], l[level]
#         permutation(l, level + 1)
#         l[level], l[i] = l[i], l[level]
#
#
# permutation(l, 0)

# 二分法
# 需求 随便一个数在列表查找（最快最便捷）
# l = [-8, 6, 9, -10, 14, 34, -3, -9, 28, 23, 8]
# num = int(input('请输入你要找的数'))
# 方法一：
# for i in l:
#     if i == num:
#         print(i)
#         break

# 二分法简单运用

# li.sort()  # 排序
# zo = int(len(l) / 2)


# num = 8
# li = [-8, 6, 9, -10, 14, 34, -3, -9, 28, 23, 8]


# def suanfa(l):
#     l.sort()
#     zo = int(len(l) / 2)
#     if l[zo] == num:
#         print(l[zo])
#     elif num > l[zo]:
#         l = l[:zo]
#         suanfa(l)
#     else:
#         l = l[zo:]
#         suanfa(l)
#
#
# suanfa(li)

# 列表的sort()函数  reverse=Ture ,则按降序排列，默认升序
