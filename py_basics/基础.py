"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 基础.py
@Author : 夏目&青一
@Time : 2022/12/10 18:17

"""
# 全局变量  global :定义全局变量
# 列表类型
# 一、容器类型
# 列表 元组 字典 集合
# 二、标量、原子类型
# 整型、浮点型、字符串


# 三、可变不可变
# a:可变类型
# 列表、字典、集合

# b:不可变类型
# 整型、浮点型、字符串、元组

# nonlocal  :非本地声明

x = 10


def hh():
    x = 20

    def hhh():
        nonlocal x  # 一层一层往外找但不会找全局！，若没有就报错
        x = 30

    print(x,'找hh本身的')
    hhh() # 开始共享
    print(x)


hh()
print(x)
