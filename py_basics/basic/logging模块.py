"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : logging模块.py
@Author : 夏目&青一
@Time : 2023/1/3 15:50

"""
# loggint模块
import logging

# WARNING:root:警告日志
# ERROR:root:错误日志
# CRITICAL:root:严重错误日志

# 日志配置
# 1.基本配置
logging.basicConfig(
    # 1、日志级别
    level=30,
    # DEBUG:10
    # INFO:20
    # WARNING:30
    # ERROR:40
    # CRITICAL:50
    # 2、日志输出格式
    format='%(asctime)s %(name)s [%(pathname)s line:%(lineno)d] %(levelname)s %(message)s',
    # 3、asctime的时间格式
    # datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
    # 4、日志输出位置：终端/文件
    # filename='user.log', # 不指定此配置，默认打印到终端
)

# 2023-01-03 16:19:18,094 root [E:\py_project\py_basics\logging模块.py line:38] WARNING 磁盘空间不足
# 2023-01-03 16:19:18,094 root [E:\py_project\py_basics\logging模块.py line:39] ERROR 错误日志
# 2023-01-03 16:19:18,094 root [E:\py_project\py_basics\logging模块.py line:40] CRITICAL 严重错误日志




logging.debug('调试日志')
logging.info("消息日志")
logging.warning('磁盘空间不足')
logging.error('错误日志')
logging.critical('严重错误日志')

# 配置字典
