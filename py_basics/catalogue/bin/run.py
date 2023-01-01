"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : run.py.py
@Author : 夏目&青一
@Time : 2023/1/1 16:12

"""
# from  ..core.core import main
import sys
import os

#  os.path.dirname(os.path.dirname(__file__))  catalogue的路径地址
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core.core import main

# main()
if __name__ == '__main__':
    main()
