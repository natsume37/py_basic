# coding : utf-8
# 夏目&青一
# @name:内置方法
# @time: 2023/1/15  19:50

# 内置方法：会在满足条件的时候自动执行
# __init__、__str__

# l = [1, 2, 3]
# l.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'<{self.name}: {self.age}>'

    def __del__(self):
        print('__del__运行了')

obj = Human('夏目', 73)
# print(obj)
# <夏目: 73>

# __del__
# 在删除对象的时候，先执行
