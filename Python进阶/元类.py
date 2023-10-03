# coding : utf-8
# 夏目&青一
# @name:元类
# @time: 2023/1/15  20:01

# 元类：实例化产生类的类
# 元类 --实例化--> 类(Human) --> 实例化 --》 对象(obj)
# 都是由元类type，实例化产生的

# Human = 元类()

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('name', self.name, 'age', self.age)


# 基于类创建的对象
# obj = Human('夏目', 73)

# print(type(obj))
# print(type(Human))
# print(type(str))
# <class '__main__.Human'>
# <class 'type'>
# <class 'type'>

# # 创建类
#
# # Human = type(........)
# # 1.类名
# class_name = 'Human'
#
# # 2.基类
# class_bases= (object,)
#
# # 3.类的子代码、产生名称空间
# class_dic = {}
# class_body = '''
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# def info(self):
#     print('name', self.name, 'age', self.age)
# '''
# exec(class_body, {}, class_dic)
# # print(class_dic)
# # {'__init__': <function __init__ at 0x0000021B5EFDBC10>, 'info': <function info at 0x0000021B5F014790>}
# #
#
# # 4.调用元类
# Human = type(class_name, class_bases, class_dic)
# print(Human)  # <class '__main__.Human'>


# raise 抛出下划线
# raise NameError('类名不能有下划线')

# 自定义元类
# class Mytype(type):
#     def __init__(self, class_name, class_bases, class_dic):
#         # print('Mytype.init')
#         if '_' in class_name:
#             raise NameError('类名不能有下划线')
#         if not class_dic.get('__doc__'):
#             raise SyntaxError('定义类必须写注释')
#
#     def __new__(cls, *args, **kwargs):
#         print('Mytype.__new__')
#
#         return super().__new__(cls, *args, **kwargs)
#
#
# # 自定义类三步骤
# # Human = Mytype(class_name, class_bases, class_dic)
# # 调用内置元类type的__call__
#     # 1.调用Mytype的__new__方法，产生一个空对象Human
#     # 2.调用__init__方法，初始化Human
#     # 3.返回初始化好的对象Human
#
# class Human(metaclass=Mytype):  # metaclass默认为type元类
#     '''
#     测试元类
#     '''
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('name', self.name, 'age', self.age)


# class Test:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, *args, **kwargs):
#         print('Test.__call__')
#         return 'abc'
#
#
# obj = Test('夏目', 18)
# obj()  # Test.__call__
# # TypeError: 'Test' object is not callable
# obj = obj()
# print(obj)


# 自定义元类
# class Mytype(type):
#     def __call__(self, *args, **kwargs):
#         human_obj = self.__new__(self)
#         self.__init__(human_obj, *args, **kwargs)
#
#         return human_obj
#
#
# class Human(metaclass=Mytype):  # metaclass默认为type元类
#     '''
#     测试元类
#     '''
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('name', self.name, 'age', self.age)
#
#     def __new__(cls, *args, **kwargs):
#         obj = super(Human, cls).__new__(cls)
#         return obj
#
# obj = Human('夏目', 18)
# # 触发Mytype的__call__方法
# #     1、调用Human的__new__方法
# #     2、调用Human__init__方法
# #     3、返回初始化的对象
#
# print(obj.__dict__)


