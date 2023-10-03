# coding : utf-8
# 夏目&青一
# @name:json文件存储、
# @time: 2023/3/6  9:36
import json

text = [
    {
        'name':'小华',
        'age':18
    },{
        'ccc':'sakldhf',
        'hsad':'sadfa'
    }
]
# dumps:把python类型转化为json格式
# loads:把json格式转化为python数据类型
res = json.dumps(text)
print(res)
