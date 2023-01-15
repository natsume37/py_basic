# coding : utf-8
# 夏目&青一
# @name:封装、继承、多态
# @time: 2023/1/15  14:45

# 封装、继承、多态
# 封装：整合


# 隐藏属性  __name  -->  _类名__name
# 并不是真正意义上的隐藏，本质是一种改名操作，在代码定义阶段就会改名，且对内不对外
# class Test:
#     __x = 10  # '_Test__x'
#
#     def __f1(self):  # '_Test__f1'
#         print('f1')
#
#
# # obj = Test()
# print(Test.__dict__)


# {'__module__': '__main__', '_Test__x': 10, '_Test__f1': <function Test.__f1 at 0x0000025C9BF3AB80>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}


# class Test:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def f1(self):
#         print(self.name)
#         print(self.age)
#
# obj = Test('xxxx', 18)
# # print(obj.name, obj.age)   # xxxx 18
# print(obj.f1())
# xxxx
# 18
# None


# 1.隐藏属性，是为了让设计者严格规范用户所传入的数值，使其不能更改数据属性
# class Test:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __f1(self):
#         print(self.name)
#         print(self.age)
#
#     # 开接口、让使用者不能直接访问，只能通过接口访问
#     def get_age(self):
#         return self.__name__name
#
#     def get_name(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         self.__age = new_age
#
#     def set_name(self, new_name):
#         if type(new_name) is not int:
#             print('你个傻子，只能传int类型')
#             return
#         if 0 <= new_name <= 100:
#             print('你个傻子，年龄必须是0-100岁')
#             return
#         self.__name = new_name

# 2.函数的隐藏  降低使用者的使用复杂性
# class Servant:
#     def __run(self):
#         print('跑起来')
#
#     def __pay(self):
#         print('付钱')
#
#     def __take_bun(self):
#         print('拿包子')
#
#     def by_bun(self):
#         self.__run()
#         self.__pay()
#         self.__take_bun()


# 类的装饰器

# class Test:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     # def __f1(self):
#     #     print(self.name)
#     #     print(self.age)
#
#     # 开接口、让使用者不能直接访问，只能通过接口访问
#     # @property   # get_age = property(get_age)
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, new_age):
#         self.__age = new_age
#
#     def set_name(self, new_name):
#         if type(new_name) is not int:
#             print('你个傻子，只能传int类型')
#             return
#         if 0 <= new_name <= 100:
#             print('你个傻子，年龄必须是0-100岁')
#             return
#         self.__name = new_name
#
#     def del_age(self):
#         del self.__age
#         return
#
#     age = property(get_age, set_age, del_age)  # 顺序不能错  查、改、删
#
#
# obj = Test('xxx', 18)
# obj.age = 20
# print(obj.age)
# del obj.age

# print(obj.get_age)  # 没有加（）调用
# 20

# property  python内置的一个装饰器
# print(property)  # <class 'property'>

# 类装饰器、语法糖进阶
# class Test:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     # def __f1(self):
#     #     print(self.name)
#     #     print(self.age)
#
#     # 开接口、让使用者不能直接访问，只能通过接口访问
#     @property  # get_age = property(get_age)
#     def age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#
#     def set_name(self, new_name):
#         if type(new_name) is not int:
#             print('你个傻子，只能传int类型')
#             return
#         if 0 <= new_name <= 100:
#             print('你个傻子，年龄必须是0-100岁')
#             return
#         self.__name = new_name
#
#     @age.deleter
#     def age(self):
#         del self.__age
#         return
#
#
# obj = Test('xxx', 18)
# obj.age = 30
# print(obj.age)


# 继承 ：创建新类的方法、通过继承创建的类叫子类、被继承的类叫父类（基类）
# 单继承  多继承（不建议使用）

# class Parent1:
#     pass
#
#
# class Parent2:
#     pass
#
#
# class Child1(Parent1):
#     pass
#
#
# class Child2(Parent1, Parent2):
#     pass
#
#
# # 查看父类的方法
# print(Child1.__bases__)
# print(Child2.__bases__)
# (<class '__main__.Parent1'>,)
# (<class '__main__.Parent1'>, <class '__main__.Parent2'>)


# 在python2里面，有新式类和经典类的区分
# 新式类：继承了object类的子类、以及继承了这个子类的子子孙孙类、python3不继承类的话、默认继承object类

# 经典类：没有继承object类的子类，以及继承了这个子类的子子孙孙类
# class Parent1(object):  # 兼用python2
#
# 继承解决类的重复

# 继承：遗传
# 多继承：可读性太差！
# 如果非要使用多继承，应该用Mixins(编程规范)！


# 父类
# class Human:
#     star = 'earth'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Chinese(Human):
#     # star = 'earth'
#     nation = 'china'
#
#     def __init__(self, name, age, gender, balance):
#         Human.__init__(self, name, age, gender)  # 派生的第三种用法
#         self.balance = balance
#
#     def speak_chinese(self):
#         print(f'{self.name}正在说普通话')
#
#
# class American(Human):
#     # star = 'earth'
#     nation = 'America'
#
#     # def __init__(self, name, age, gender):
#     #     self.name = name
#     #     self.age = age
#     #     self.gender = gender
#
#     def speak_english(self):
#         print(f'{self.name} is speaks english')
#
#
# dy_obj = Chinese('夏目', 18, '男',10000)
# print(dy_obj.__dict__)
# # {'name': '夏目', 'age': 18, 'gender': '男', 'balance': 10000}
# print(dy_obj.nation)
# # china
# dy_obj.speak_chinese()
# # 夏目正在说普通话
# da_obj = American('jurn', 20, '男')

# 属性查找过程
# 对象-Python进阶-父类....object
# class Test1:
#     def f1(self):
#         print('Test.f1')
#
#     def f2(self):
#         print('Test1.f2')
#         self.f1()  # 此时 self = obj
#
#
# class Test2(Test1):
#     def f1(self):
#         print('Test2.f1')
#
#
# obj = Test2()
# obj.f2()
# 结果
# Test1.f2
# Test2.f1

# 多继承属性查找
# MRO列表。 C3算法实现

# 凌型问题（钻石问题）
# class A:
#     def f1(self):
#         print('A.f1')
#
#
# class B(A):
#     def f1(self):
#         print('B.f1')
#
#
# class C(A):
#     def f1(self):
#         print('C.f1')
#
#
# class D(B, C):
#     def f2(self):
#         print('D.f2')
#
#
# print(D.mro())  # MRO列表
# # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#
# obj = D()
# obj.f1()
# 结果
# B.f1


# 非凌型查找  一个分支找完再找其他分支（object一定最后找）

# 凌型继承 ：一个分支找完再找其他分支（经典类：深度优先查找）

# 新式类：广度优先查找   找完最后一条分支后再找最终的父类


# 1.继承结构不要太复杂
# 2.满足什么是什么的关系


# MixIns机制 #通过一些命名的规范,来提高代码的可读性
# MixIn able ible做后缀
# 责任要单一，独立的插件
# class Fowl:  # 真正意义上的父类
#     pass
#
#
# class SwimMixin:  # 只是混入一些功能，理解上不能算父类
#     def swimming(self):
#         pass
#
#
# class Chicken(SwimMixin, Fowl):
#     pass
#
#
# class Duck(SwimMixin, Fowl):
#     pass


# super
# # 父类
# class Human:
#     star = 'earth'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Chinese(Human):
#     # star = 'earth'
#     nation = 'china'
#
#     def __init__(self, name, age, gender, balance):
#         # python2必须这么用  》》》》super 一定是mro列表的下一个列表开始找！！！
#         super(Chinese, self).__init__(name, age, gender)  # super 关系绑定型
#         # python3可以省略参数
#         super().__init__(name, age, gender)  # super 关系绑定型
#         self.balance = balance
#
#     def speak_chinese(self):
#         print(f'{self.name}正在说普通话')
#
#
# class American(Human):
#     # star = 'earth'
#     nation = 'America'
#
#     # def __init__(self, name, age, gender):
#     #     self.name = name
#     #     self.age = age
#     #     self.gender = gender
#
#     def speak_english(self):
#         print(f'{self.name} is speaks english')
#
#
# dy_obj = Chinese('夏目', 18, '男', 10000)
# print(Chinese.mro())
# # [<class '__main__.Chinese'>, <class '__main__.Human'>, <class 'object'>]
# # supper 会从当前列表的下一个mro列表开始查找 P364行
# print(dy_obj.__dict__)
# # {'name': '夏目', 'age': 18, 'gender': '男', 'balance': 10000}


# 多态(是一种编程思想)  --》继承
# 汽车：奔驰、理想、奥托
# class Car:
#     def run(self):
#         print('开始跑', end=' ')
#
#
# class Benci(Car):
#     def run(self):
#         super(Benci, self).run()
#         print('加98号汽油')
#
#
# class lx(Car):
#     def run(self):
#         super(lx, self).run()
#         print('加93号汽油')
#
#
# car1 = Benci()
# car2 = lx()
# car1.run()
# car2.run()
# # 开始跑 加98号汽油
# # 开始跑 加93号汽油


# 鸭子类型
# linux: 一切皆文件
# 抽象基类  abc模块


# 类方法
# import settings
#
#
# class Mysql:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     def f1(self):
#         print(self.ip, self.port)
#
#     @staticmethod     # 非绑定方法 （一个普通函数-静态方法）
#     def f2():
#         print('hhhh')
#
#     @classmethod
#     def instance_from_conf(cls):  # 动态的cls-->类名
#         print(cls)
#         obj = cls(settings.IP, settings.PORT)
#         return obj
#
#
# res = Mysql.instance_from_conf()
# print(res.__dict__)
# <class '__main__.Mysql'>
# {'ip': '120.0.0.1', 'port': 3306}
