# coding : utf-8
# 夏目&青一
# @name:反射机制
# @time: 2023/1/15  19:27

# 反射机制

# def f1(obj):
#     if 'age' not in obj.__dict__:
#         return
#
#     obj.age
#
# f1(18)
# AttributeError: 'int' object has no attribute '__dict__'


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('name', self.name, 'age', self.age)


obj = Human('夏目', 18)

# dir()获取有用属性
# print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'info', 'name']


# 内置函数
# hasattr()     判断是否存在，返回布尔值
# getattr()     获取对象值
# setattr()     更改对象值
# delattr()     删除对象值
#

# print(hasattr(obj, 'name'))  # True
# print(getattr(obj, 'name'))  # 夏目
# setattr(obj, 'name', '李白')
# print(obj.name)     #李白
# delattr(obj, 'name')
# print(obj.name)
# AttributeError: 'Human' object has no attribute 'name'


# 案例
# if hasattr(18, 'age'):
#     print(getattr(18, 'age'))
# else:
#     print('没有age')

# 没有age

# print(getattr(obj, 'age', None))
# 18
