# coding : utf-8
# 夏目&青一
# @name:单例模式
# @time: 2023/1/15  21:10

# 单例模式  解决类在实例化时内存地址的浪费问题
# 1、模块导入
# from settings import obj
# from settings import obj
# from settings import obj


# 2、类装饰器
# def singleton_mode(cls):
#     obj = None
#     def wrapper(*args, **kwargs):
#         nonlocal obj
#         if not obj:
#             obj = cls(*args, **kwargs)
#         return obj
#     return wrapper
#
#
# @singleton_mode
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# obj1 = Human('夏目', 28)
# obj2 = Human('夏目', 18)
# print(obj1)
# print(obj2)

# 3、类绑定方法
# class Human:
#     obj = None
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def get_obj(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = cls(*args, **kwargs)
#         return cls.obj
#
#
# obj1 = Human.get_obj('夏目', 28)  # !!
# obj2 = Human.get_obj('夏目', 28)
# print(obj1)
# print(obj2)

# 4、__new__方法
# class Human:
#     obj = None
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.obj:
#             cls.obj = super().__new__(cls)
#         return cls.obj
#
#
# obj1 = Human('夏目', 28)  # !!
# obj2 = Human('夏目', 28)
# print(obj1)
# print(obj2)


# 5、元类
class Mytype(type):
    obj = None

    def __call__(self, *args, **kwargs):
        if not self.obj:
            self.obj = super().__call__(*args, **kwargs)
        return self.obj


class Singleton(metaclass=Mytype):
    pass


class Human(Singleton):
    obj = None

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Human('夏目', 28)  # !!
obj2 = Human('夏目', 18)
print(obj1)
print(obj2)
# 6、并发
