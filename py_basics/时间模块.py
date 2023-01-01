"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 时间模块.py
@Author : 夏目&青一
@Time : 2023/1/1 23:52

"""
# time
import time
# 1.时间戳
# print(time.time())

# 2.格式化的字符串：2030-11-11 11:11:11   字符串类型
# print(time.strftime("%Y-%m-%d %H:%M:%S"))  2023-01-01 23:55:17
# print(time.strftime("%Y-%m-%d %H:%M:%S %A")) 2023-01-01 23:56:49 Sunday
# print(time.strftime("%x %X %A")) 01/01/23 23:57:29 Sunday

# 3.结构化时间
# res = time.localtime()
# print(res)
# time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1,
# tm_hour=23, tm_min=59, tm_sec=11, tm_wday=6, tm_yday=1, tm_isdst=0)

# datatime
import datetime

# res = datetime.datetime.now()
# print(res.replace(microsecond=0))  # 2023-01-02 00:02:03  microsecond(微秒)

# 时间的加减
# res = datetime.datetime.now() + datetime.timedelta(days = 23)
# print(res.replace(microsecond=0)) # 2023-01-25 00:05:20

# 时间戳 --localtime/gmtime--> 结构化的时间 --strftime--> 格式化的字符串时间
# 时间戳 <--mktime-- 结构化的时间 <--strptime-- 格式化的字符串时间
# t = '1983-12-07 01:02:03'
# print(time.strptime(t,
#                     '%Y-%m-%d %X'))  # time.struct_time(tm_year=1983, tm_mon=12, tm_mday=7, tm_hour=1, tm_min=2, tm_sec=3, tm_wday=2, tm_yday=341, tm_isdst=-1)
# res = time.strptime(t, '%Y-%m-%d %X')
# print(time.mktime(res))  # 439578123.0

# time.sleep()
# print(time.asctime())  # Mon Jan  2 00:17:56 2023
# time.ctime()

# 小项目 ：随机生成一个16位的密码包括大写字母，小写字母，数字和符号
import random

def pwd_gener(length=16):
    pwd = ''
    char_list = [[97, 122], [65, 90], [48, 57], [33, 47]]
    for _ in range(length):
        random_list = random.choice(char_list)
        random_char = chr(random.randint(*random_list))  # 打散  类似于 random_list[0], random_list[1]
        # chr  ASKL码转字符串
        pwd += random_char
    print(pwd)
    # 外加判断

pwd_gener(15)
