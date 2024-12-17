# 封装

class User(object):
    def __init__(self, name, age):
        self._name = name # 受保护的变量
        self.__age = age  # 双下划线表示私有变量
        pass

    @property
    def get_age(self):
        print('Function get_age triggered')
        return self.__age

    @property # 获取变量
    def age(self):
        print('Function age triggered')
        return self.__age

    @age.setter # 修改变量用的
    def age(self, age):
        print('Function set_age triggered')
        self.__age = age

    def show_infos(self):
        print('User::show_infos function triggered')

    def _show_infos1(self):
        print('User::_show_infos1 function triggered')

    def __show_infos2(self):
        print('This function can not be called outside')

mia = User('mia', 24)
print(mia.age)
mia.age = 42
print(mia.age)


# print(mia._name) # 代码是上是允许的, 只是口头约定
# mia.show_infos()
# mia._show_infos1()
#
# print(mia._User__age)    # 绕过 private 这个机制
# mia._User__show_infos2() # 绕过 private 这个机制
#
# print(dir(mia)) # 打印所有属性和方法

# mia.name = 'Tom'
# mia.age = 25
# print(mia.__dict__)