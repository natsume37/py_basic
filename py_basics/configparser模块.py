"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : configparser.py
@Author : 夏目&青一
@Time : 2023/1/2 1:20

"""
# configparser模块  （专业的配置文件格式）
import configparser

config = config = configparser.ConfigParser()
config.read('data/test.ini', encoding='utf-8')
# print(config.sections())  # ['标题', 'db']
# print(config.options('db'))  # ['db_type', 'name']
# print(config.items('db'))  # [('db_type', 'mysql'), ('name', 'xiamu')]

delay = config.get('db', 'name')
print(delay, type(delay))  # xiamu <class 'str'>
delay = config.getint('db', 'name')
delay = config.getfloat('db', 'name')
delay = config.getboolean('db', 'name')  # 布尔值

