list3 = list('1234567890')
print(list3[3])
print(len(list3))
print(max(list3))
print(min(list3))

list2 = [1,2,3,'a', 'b', False]

for x in list2:
    print(f"x = {x}")

for index, value in enumerate(list2):
    print(f"index = {index}, value = {value}")

# 常用函数
list2.append(6666)    # append 的是元素
list2.extend([1,2,3]) # extend 是给列表的
list2.insert(2, 'vin')
list2.pop(2)
del(list2[2])
list2.remove(2)
print(list2)

del list3 # 删除整个变量的定义
# print(list3) # 这个将会出错

