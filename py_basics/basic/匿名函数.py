"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 匿名函数.py
@Author : 夏目&青一
@Time : 2022/12/15 15:49

"""

# 有名函数
# def func(x, y):
#     return x + y


# 匿名函数 lambda
"""
匿名函数自带return，且没有回车
匿名函数只需要再定义的时候调用一下，随后调用计数为零被回收
应用场景： 不需要重复操作，临时用一下！
"""
# (lambda x, y: print(f'这是函数子代码 功能是打印下，y{x, y}'))(1, 2)  # 返回值为None
# res = (lambda x, y: x + y)(1, 2)  # 返回值 x + y

# 匿名函数的应用场景

#  需求给定字典求收入最大的是哪个

# info = {
#     '柯南': 10000,
#     '小黑': 3000,
#     '小兰': 20000,
#     '灰原哀': 90000
# }
# 原方案
# def func(k):
#     return info[k]
# res = max(info,key=func)
# print(res)

# 匿名函数
# res = max(info, key=lambda k: info[k])  # key参数初识
# print(res)
# res = min(info, key=lambda k: info[k])
# print(res)

# sort(key=)

# 需求 按元组的第二个值排降序
# l = [(1, 2), (3, 4), (2, 1), (4, 3)]
# l.sort(key=lambda num:num[1]) # [(2, 1), (1, 2), (4, 3), (3, 4)]


# 结尾添加  老坛酸菜
# l = ['康师傅', '统一', '白象', '大今野', '红烧']

# l= [i+"老坛酸菜" for i in l]  # ['康师傅老坛酸菜', '统一老坛酸菜', '白象老坛酸菜', '大今野老坛酸菜', '红烧老坛酸菜']
# l= (i+"老坛酸菜" for i in l)  # 变成生成器，不用考虑内存撑爆问题

## map()函数 ： 也是生成器
# res = map(lambda name: name + '老坛酸菜', l)
# print(res)  # <map object at 0x0000024CDE84F220>   --生成器
# print(res.__next__()) # 康师傅老坛酸菜
# print(res.__next__()) # 统一老坛酸菜
# print(res.__next__()) # 白象老坛酸菜


# 函数的提示类型 3.5以后
# def func(x: str, y: int) -> int:  # -> 提示返回值为int
#     print(x)
#     print(y)
#     return 10
#
# def func2(x: '你好呀', y: int = 88) -> int:  # -> int = 88 相当于 y = 88
#     print(x)
#     print(y)
#     return 10
#
# func2()

# 查看函数的提示信息
# print(func2.__annotations__)