class Player(object):  # object 基类
    def __init__(self, name, age, city):  # 构造函数, self 其实就代表了实例化对象
        self.name = name
        self.age = age
        self.city = city

    def show(self):
        print("THis is a function in Player::show")


class VIP(Player):
    def __init__(self, name, age, city, level):
        super().__init__(name, age, city)
        self.level = level


mia = VIP('mia', 42, 'SH', 3)
print(type(mia))
print(isinstance(mia, Player))
print(isinstance(mia, VIP))
mia.show()