"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : hash算法.py
@Author : 夏目&青一
@Time : 2023/1/2 18:02

"""
# hash(哈希)
# md5   已破解
# sha1  已破解
# sha256
# sha512

# hash值
# 1.输入敏感
# 2.不可逆
# 3.计算极快而长度固定


# 使用

# import hashlib

# h1 = hashlib.md5()
# # h1.update(二进制数据)
# h1.update('abc'.encode('utf-8'))
# h1.update('123'.encode('utf-8'))
# print(h1.hexdigest())  # abc123的运算结果    e99a18c428cb38d5f260853678922e03e99a18c428cb38d5f260853678922e03

# h1 = hashlib.sha512('ab'.encode('utf-8'))
# # h1.update(二进制数据)
# h1.update('c'.encode('utf-8'))
# h1.update('123'.encode('utf-8'))
# print(h1.hexdigest())
# c70b5dd9ebfb6f51d09d4132b7170c9d20750a7852f00680f65658f0310e810056e6763c34c9a00b0e940076f54495c169fc2302cceb312039271c43469507dc


# 大文件完整性校验： 选取个别点做校验（例如每次取文件的1/10然后比较）

# 1.import os  # 计算文件大小
# 2。
# path = r'E:\py_project\py_basics\catalogue\log\user.log'
#
#
# m = hashlib.md5()
# with open(path, 'rb') as f:
#     f.seek(0, 2)  # 文件指针操作
#     size = f.tell()
#     print(size)  # 1538
#
#     one_tenth = size // 10
#     for i in range(10):
#         f.seek(i*one_tenth, 0)
#         res = f.read(100)  # 读取100个字节 做样本比较
#         m.update(res)
#     print(m.hexdigest()) # 69ed1450e1e151ef047e538f53819e9b


# 密码加盐
pwd = 'hhahah'

import hashlib

m = hashlib.md5()
m.update('夏目最帅'.encode('utf-8'))  # 加盐
m.update(pwd.encode('utf-8'))
m.update('猫咪老师最可爱'.encode('utf-8'))  # 加盐
print(m.hexdigest())  # 2aed6719b023a5e09e96cb17496cc415

