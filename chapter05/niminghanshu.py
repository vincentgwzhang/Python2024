# def f(a,b):
#     return a+b
#
# result = f(1,2)
# fun = lambda a,b:a+b
# print(fun(1, 3))

# a = [1,2,3,4,5]
# b = []
# for i in range(len(a)):
#     a[i] = a[i] ** 2
#
# print(a)

def f(x, y):
    return x**y

a = [1,2,3,4,5]
b = [3,3,3,3,3]
result = map(f, a, b)
print(list(result))

# Reduce
from functools import reduce
print(reduce(lambda x,y:x+y, a))


a = [1,2,3,4,5]
result = filter(lambda x: x!=0, a)
print(list(result))

a = ["1", '2', '3s']
for s in a[::-1]:
    print(s)
