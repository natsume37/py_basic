"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 函数.py
@Author : 夏目&青一
@Time : 2022/12/10 18:45

"""

# 函数名就是函数的内存地址 可传递

# 电子钱包
# def login():
#     print('执行登录功能')
#
#
# def scan():
#     print('执行扫码功能')
#
#
# def tranfer():
#     print('执行转账功能')
#
#
# def query():
#     print('执行查询余额功能')


# while True:
#     print("""
#     0   退出
#     1   登录
#     2   扫码
#     3   转账
#     4   查询余额
#     """)
#     c = input('请输入选项>>>')
#     if c == '0':
#         print('欢迎下次再来')
#         break
#     if c == '1':
#         login()
#     elif c == '2':
#         scan()
#     elif c == '3':
#         tranfer()
#     elif c == '4':
#         query()
#     else:
#         print('重新输入，笨蛋')

# 电子钱包优化  字典解决，防止无限的elif

# func_dic = {'1': login, '2': scan, '3': tranfer, '4': query}
# while True:
#     print("""
#         0   退出
#         1   登录
#         2   扫码
#         3   转账
#         4   查询余额
#         """)
#     opt = input('请输入功能编号>>>')
#     if opt == '0':
#         print('已安全退出')
#         break
#     if opt not in func_dic:  # 美观，代码规范
#         print('输入有毛病，傻子')
#         continue
#
#     func_dic[opt]()  # 美观，代码规范

# 电子钱包3优化  ！！！while彻底不用改了！！！
import time

"""def login():
    print('执行登录功能')


def scan():
    print('执行扫码功能')


def tranfer():
    print('执行转账功能')


def query():
    print('执行查询余额功能')


func_dic = {
    '0': (None, '提出'),
    '1': (login, '登录'),
    '2': (scan, '扫码'),
    '3': (tranfer, '转账'),
    '4': (query, '查询')
    }
while True:
    for key in func_dic:
        print(key,func_dic[key][1])
    opt = input('请输入功能编号>>>').strip()
    if opt == '0':
        print('已安全退出')
        break
    if opt not in func_dic:  # 美观，代码规范
        print('输入有毛病，傻子')
        continue

    func_dic[opt][0]()  # 美观，代码规范
"""

# 闭包函数
"""def f1(x):

    def f2():
        print(x)

    return f2


res = f1(20)
print(res)  # 局部的作用域拿到全局调用！！！！
res()"""

# 装饰器 ！！！！！
# 定义一个函数去修饰另一个函数 给其他函数添加额外的功能
# 开放封闭原则

# 增加时间统计功能  不修改源代码，不修改调用方式，代码不臃肿  小飞有点东西  224集
# import time
#
#
# def insider(nb, t):
#     print('欢迎来到和平精英')
#     print(f'你队友都是{nb}')
#     print(f'飞机还有{t}秒起飞了')
#     time.sleep(t)
#     print('飞机已经起飞了')
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         star = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'耗时{end - star}')
#
#     return wrapper
#
#
# insider = outer(insider)
# insider('傻叉', 4)
# 上述代码好处是可适用其他任何函数  但是！！！！---  会丢失原函数的返回值  --！！！
# ----------------------------------------------------------------------------


# 方案六
"""import time


# def insider(nb, t):
#     print('欢迎来到和平精英')
#     print(f'你队友都是{nb}')
#     print(f'飞机还有{t}秒起飞了')
#     time.sleep(t)
#     print('飞机已经起飞了')


def recharge(num):
    for i in range(num,101):
        time.sleep(0.05)
        print(f'\r当前电量为{"#"*i} {i}%', end='')
    print('  电量已充满')
    return 100


def outer(func):
    def wrapper(*args, **kwargs):
        star = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'耗时{end - star}')

    return wrapper


recharge = outer(recharge)
r = recharge(20)
print(r)  # 无返回值！！"""


#  以上代码没有返回值，不符合装饰原则！！！

# 方案七
# import time
#
#
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量为{"#" * i} {i}%', end='')
#     print('  电量已充满')
#     return 100
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         star = time.time()
#         response = func(*args, **kwargs)  # 重点
#         end = time.time()
#         print(f'耗时{end - star}')
#         return response  # 重点
#     return wrapper
#
# recharge = outer(recharge)
# re = recharge(20)
# print(re)  # 得到返回值


# 语法糖  @function
# import time
#
#
# def count_time(func):
#     def wrapper(*args, **kwargs):
#         star = time.time()
#         response = func(*args, **kwargs)  # 重点
#         end = time.time()
#         print(f'耗时{end - star}')
#         return response  # 重点
#
#     return wrapper
#
#
# @count_time  # 相当于count_time(recharge)   等价于 recharge = count_time(recharge)
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量为{"#" * i} {i}%', end='')
#     print('  电量已充满')
#     return 100
#
#
# @count_time
# def insider(nb, t):
#     print('欢迎来到和平精英')
#     print(f'你队友都是{nb}')
#     print(f'飞机还有{t}秒起飞了')
#     time.sleep(t)
#     print('飞机已经起飞了')
#
#
# recharge(20)
# insider('sb', 2)


# 装饰器基本模型
# import time
#
#
# def login(func):
#     def wrapper(*args, **kwargs):
#         name = input('请输入姓名').strip()
#         pwd = input('请输入密码').strip()
#         if name == 'hh' and pwd == '123':
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('密码错误')
#
#     return wrapper
#
#
# @login
# def home():
#     """文档注"""
#     time.sleep(2)
#     print('welcome')


# 完美但并不绝对完美
# for example
# print(home)
# print(home.__name__)
# print(home.__doc__)  # None
# 低级方案
# home.__name__ =' home'
# home.__doc__ = """文档注释"""


# 完美装饰器！！！
# home.__name__ = 原函数地址.__name__
# home.__doc__ = 原函数地址.__doc__

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper

# 但是不切合实际
# from functools import wraps  # !!!
# import time
#
#
# def login(func):
#     @wraps(func)  # 把原函数所有属性赋值给wrapper!!!!
#     def wrapper(*args, **kwargs):
#         name = input('请输入姓名').strip()
#         pwd = input('请输入密码').strip()
#         if name == 'hh' and pwd == '123':
#             res = func(*args, **kwargs)
#             return res
#         else:
#             print('密码错误')
#
#     return wrapper
#
#
# @login
# def home():
#     """文档注释"""
#     time.sleep(2)
#     print('welcome')
#
#
# print(home.__doc__)
# print(home.__name__)

# 有参修饰器

# def g_outer(name,age):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(name,age)
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#     return outer
#
#
# @g_outer('夏目',19)  # outer = w("夏目")  内存地址的递归  到此，全部结束
# def hh():
#     print('你好')
#
#
# hh()


# 有参装饰器模板
# def g_outer(x):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#     return outer


# 有参装饰器应用
#

# 装饰器的叠加

# @outer2
# @outer2
# @outer1
# 加载顺序   自上而下！
