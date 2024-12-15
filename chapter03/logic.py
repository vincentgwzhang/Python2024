# 一元运算符优先级是最高的
# not > and > or

print(None and 'hi') # 结果返回 None
print('hi' and None) # 结果返回 None
print('hi' and '') # 结果返回空值
print('' and 'hi') # 结果返回空值
print(0 and 1) # 结果返回 0
print(1 and 0) # 结果返回 0
# 上面的思想其实一样的


print(1 and 2) # 结果返回 2
print(2 and 1) # 结果返回 1
print(1 and 'a') # 结果返回 a
print('a' and 1) # 结果返回 1
print('a' and 'a') # 结果返回 a
# 上面的思想其实一样的
print("================================")
print(1 or 0)
print(0 or '' or 888)
print("================================")
print(not 'hello')
print(not 1)
