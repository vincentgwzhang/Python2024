d = {
    'name': 'mia',
    'gender': False,
}

print(d)
print(type(d))

# add
d['height'] = 180
print(d)

# check
print('height' in d)

# enumerate
for key in d:
    print(f"key = {key}, value={d[key]}")

for key,value in d.items():
    print(f"key = {key}, value={value}")

for key in d.keys():
    print(f"key = {key}")

for value in d.values():
    print(f"value = {value}")

d.pop('height')
e = d.copy() # 这是深度复制
d['gender'] = True
print(e['gender'])


d.update


# 用法1：使用字典更新
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # 输出：{'a': 1, 'b': 3, 'c': 4}


# 用法2：使用键值对更新
d = {"a": 1}
d.update(b=2, c=3)
print(d)  # 输出：{'a': 1, 'b': 2, 'c': 3}



# 用法3：与其他可迭代对象结合
d = {"a": 1}
d.update([("b", 2), ("c", 3)])
print(d)  # 输出：{'a': 1, 'b': 2, 'c': 3}

