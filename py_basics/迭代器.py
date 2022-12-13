"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 迭代器.py
@Author : 夏目&青一
@Time : 2022/12/11 10:38

"""


# 迭代器  ： 不依赖索引取值的方式

# num = 0
# while True:
#     print(num)
#     num += 1

# l = ['a', 'b', 'c']
# num = 0
# while num < len(l):
#     print(l[num])
#     num += 1

# 可迭代对象  内置有 __iter__方法
# 迭代器对象  内置有 __iter__  以及 __next__ 的对象

# d = {'key1':1, 'key2': 2, 'key3':3}
# res = d.__iter__() # 得到迭代器对象 已固定，用完就消失

# print(res.__next__()) # 通过__next__方法依此获取里面的值   key1
# print(res.__next__()) # key2
# print(res.__next__()) # key3
# # print(res.__next__())   抛异常


# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break

# 迭代循环  for循环
# d = {'key1':1, 'key2': 2, 'key3':3}

# 1、调用迭代对象或者可迭代对象的 __iter__方法
# 2、再调用对象的 __next__方法，赋值给i,并循环调用
# 3、检测异常，抛出异常后结束循环
# for i in d:
#     print(i)

# 生成器  yield（生成迭代器）  jc_P250
# def func():
#     print('这是第一次执行')
#     yield 1
#     print('这是第二次执行')
#     yield 2
#     print('这是第三次执行')
#     yield 3
#     print('这是第四次执行')
#     yield 4
#     print('这是第五次执行')


 # 没内容  func()
res = func()  # res 生成器（自定义的迭代器）

# print(res.__iter__())  # itere(res)
# print(res.__next__())
# print(next(res))
# print(next(res))

