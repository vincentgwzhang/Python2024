import random

# 0 - 1
a = random.random()

a = random.randint(1, 22)

list1 = [1,2,3,4,5,6]

print(list1[random.randint(0, len(list1)-1)])
print(random.choice(list1))
print(random.choice('abcdefghijkl'))

# 生成一个随机字母组成的列表
a = []
for i in range(20):
    t = random.randint(65, 90)
    a.append(chr(t))
print(a)