# coding : utf-8
# 夏目&青一
# name:
# time:
class Hero:
    def __init__(self):
        self.work = '射手'
        print('你好')

    def hhh(self):
        print(self.work)

    print('1'.center(20, '+'))  # 定义阶段就被调用


# print(Hero.__dict__)
# {'__module__': '__main__', '__init__': <function Hero.__init__ at 0x000002BF2375AB80>, 'hhh': <function Hero.hhh at 0x000002BF2375AF70>, '__dict__': <attribute '__dict__' of 'Hero' objects>, '__weakref__': <attribute '__weakref__' of 'Hero' objects>, '__doc__': None}

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()
print(hero1.__dict__)

# 添加属性
# hero1.__dict__['name'] = '鲁班七号'
# hero1.__dict__['speed'] = 450
# hero1.__dict__['name'] = '后裔'

# .方法
# hero1.name = '鲁班七号'
# hero1.speed = 450
# hero1.name = '后裔'
# print(hero1.__dict__)
# # {'work': '射手', 'name': '后裔', 'speed': 450}


