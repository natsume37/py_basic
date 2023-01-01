"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : settings.py
@Author : 夏目&青一
@Time : 2023/1/1 16:13

"""

import os

#  os.path.dirname(os.path.dirname(__file__))  catalogue的路径地址
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_PATH = rf'{BASE_DIR}\log\user.log'
