def f(a, b=6, c=2):
    print(f"a + b  + c = {a + b + c}")

f(2,3)
f(2, c = 3)

print("-" * 30)

# 函数为可变参数
def total(*args):
    result = 0
    for i in args:
        result += i
    print(f"result = {result}")

total(1, 2, 3)

print("-" * 30)

# key word args, 接收字典
def f(**kwargs):
    for k,v in kwargs.items():
        print(f"k = {k}, v = {v}")

d = {'name': 'vincent', 'age': 18}
f(**d)

print("-" * 30)
gnum1 = 20
def f2():
    global gnum1 # 修改整个global 的变量
    gnum1 = 202

f2()
print(gnum1)

print("-" * 30)

fun = lambda a,b: a+b
print(fun(2, 3))
