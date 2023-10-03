"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 三元表达式.py
@Author : 夏目&青一
@Time : 2022/12/11 11:31

"""

# 三元表达式
# 比较两数大小
# def max(x, y):
#     if x > y:
#         return x
#     elif x < y:
#         return y
#     else:
#         print('一样大')
#
# max = max(2,4)
# print(max)


# 高级写法  if 条件 else 不成立返回的值
# x = 100
# y = 20
# res = x if x > y else y
# print(res)


# 列表生成式

# l = ['康师傅——老坛酸菜', '统一——老坛酸菜', '大敬业——老坛酸菜', '白象']
# new_lis = []
# for i in l:
#     if i.endswith('老坛酸菜'):
#         new_lis.append(i)
# print(new_lis)

# 列表生成式
# l = ['康师傅——老坛酸菜', '统一——老坛酸菜', '大敬业——老坛酸菜', '白象']
# new_lis = [name for name in l if name.endswith('老坛酸菜')]
# print(new_lis)



# 没有元组生成式！！！只能是生成器！！ generator
# 生成器表达式
# l = ['康师傅——老坛酸菜', '统一——老坛酸菜', '大敬业——老坛酸菜', '白象']
# res = (name for name in l)  # 调用一次产生一个值，绝对节省内存空间
# # print(res,type(res))
# print(next(res))  # 康师傅——老坛酸菜
# print(next(res))  # 统一——老坛酸菜
# print(res.send(100))  # 大敬业——老坛酸菜


# 查看文件字符个数
# with open('user.log',mode='rt',encoding='utf-8')as f:
    # 方案一
    # size = 0
    # for line in f:
    #     len(line)
    #     size += len(line)

    # 方案二
    # size = sum([len(line) for line in f]) # 但列表有时很大，也是不安全，内存溢出
#     size = sum((len(line) for line in f))  # 等价于 sum(len(line) for line in f) 产生 生成器对象，用一次产生一个值，相对来说最理想
# print(size)

