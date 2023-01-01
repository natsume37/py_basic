"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : common.py
@Author : 夏目&青一
@Time : 2023/1/1 23:30

"""

import time
from conf.settings import LOG_PATH

def logger(msg):
    with open(LOG_PATH, mode='at', encoding='utf-8') as f:
        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {msg}\n')