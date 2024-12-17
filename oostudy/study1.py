class Player(object):  # object 基类
    def __init__(self, name, age, city):  # 构造函数, self 其实就代表了实例化对象
        self.name = name
        self.age = age
        self.city = city


tom = Player('Tom', 24, 'Shanghai')  # 类的实例化
# print(tom.__dict__)
# print(type(tom.__dict__))  # 字典
tom.name2 = 'Tom'  # 属性是可以动态添加的
tom.age = 24


# print(type(tom))
# print(isinstance(tom, Player)) # true

# 武器: 攻击值
class Weapon(object):
    numbers = 110

    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

    def show(self): # 实例方法
        print('Function show triggered')

    @classmethod # 表示这是个属于类的方法
    def get_players(cls):
        print('Function get_players triggered')

    @staticmethod
    def isValid(**kwargs):
        return kwargs['age'] > 18

gun = Weapon('Minigun', 2000, 5)
#print(Weapon.numbers)
#gun.show()
#Weapon.get_players()
#gun.get_players()
infos = {'a': 'a_v', 'b': 'b_v', 'c': 'c_v', 'age': 200}

print(Weapon.isValid(**infos))