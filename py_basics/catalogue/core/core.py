"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : core.py.py
@Author : 夏目&青一
@Time : 2023/1/1 16:22
"""
from lib.common import logger


def login():
    print('执行登录操作'.center(30, '*'))
    logger("夏目登录了")

def register():
    print('注册功能'.center(30, '*'))
    logger('夏目注册了')

def rechaarge():
    print('执行充值功能'.center(30, '*'))
    logger('夏目注册了')

def transfer():
    print('执行转账功能'.center(30, '*'))
    logger('夏目转账了')

func_dic = {
    '0': ('退出', exit),
    '1': ('退出', login),
    '2': ('退出', register),
    '3': ('退出', rechaarge),
    '4': ('退出', transfer),
}


def main():
    while True:
        for key in func_dic:
            print(key, func_dic[key][0])
        opt = input('请输入功能编码》》》').strip()
        if opt not in func_dic:
            print('\033[33m输入有误，请重新输入！\033[0m')  # 输出黄色文字
            continue
        func_dic[opt][1]()
