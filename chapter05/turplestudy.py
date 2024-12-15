tuple1 = (1,2,3,True, 'hello')
print(type(tuple1))
tuple2 = (1, ) # 元组里面只有一个元素的时候必须加逗号
print(type(tuple2))
tuple3 = ()
print(type(tuple3))
tuple4 = (1)
print(type(tuple4)) # 这个变成 <class 'int'>
tuple5 = ('abc')
print(type(tuple5))
tuple6 = ([1,3,4,5])
print(type(tuple6))
print("=" * 50)
print(tuple1[2])
print(tuple1[::-1])
print(max((1,2,3)), min((4,5,6)))
print((1,2) + (3,4))
print((1,2) * 3)
print(1 in (1,2,3))
print("=" * 50)
print(tuple1.index('hello'))
print(tuple1.index(3))
for i in tuple1:
    print(f" i = {i}")

for index, value in enumerate(tuple1):
    print(f"index = {index}, value = {value}")

