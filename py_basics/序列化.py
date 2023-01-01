"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : 序列化.py
@Author : 夏目&青一
@Time : 2023/1/2 0:40

"""
# 序列化和反序列化
# 序列化：把内存中的数据类型转化成一种特定格式，可以用于存储，或者传输给其他设备（jison）

# 内存中的数据类型 --> 序列化 --> 特定格式（json/pickle）
# 内存中的数据类型 <-- 反序列化 <-- 特定格式（json/pickle（Python专用格式））

# 用途：
# 1.存档
# 2.跨平台数据交互

# json模块
# 1.序列化
# import json

# dic = {
#     'name': '夏目', 'age': '18', 'salar': 3.5, 'marrid': False
# }
# json_res1 = json.dumps(dic)
# print(json_res1)
# # {"name": "\u590f\u76ee", "age": "18", "salar": 3.5, "marrid": false}
# json_res2 = json.dumps(dic,ensure_ascii=False)
# print(json_res2,type(json_res2))
# # {"name": "夏目", "age": "18", "salar": 3.5, "marrid": false} <class 'str'>

# 2.反序列化
# dic = json.loads('{"name": "夏目", "age": "18", "salar": 3.5, "marrid": false}')
# print(dic)
# {'name': '夏目', 'age': '18', 'salar': 3.5, 'marrid': False}


# pickle
dic = {
    'name': '夏目', 'age': '18', 'salar': 3.5, 'marrid': False, 's': {1, 2, 3}
}

import pickle

# pickle_res = pickle.dumps(dic,protocol=0)  # protocol=0 解决乱码问题
# print(pickle_res,type(pickle_res))
# b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x06\xe5\xa4\x8f\xe7\x9b\xae\x94\x8c\x03age\x94\x8c\x0218\x94\x8c\x05salar\x94G@\x0c\x00\x00\x00\x00\x00\x00\x8c\x06marrid\x94\x89\x8c\x01s\x94\x8f\x94(K\x01K\x02K\x03\x90u.' <class 'bytes'>
with open('data/text2.pickle', mode='wb')as f:
    pickle.dump(dic,f,protocol=0)


# 古老的交互式类型
# xml