# x = 1
# sum = 0
# while x < 101:
#     sum = sum + x
#     x = x + 1
#
# print(f"x finally equals to {x}")
# print(f"sum finally equals to {sum}")
# print("========================================================")


x = 1
sum = 0
while x < 5:
    sum = sum + x
    x = x + 1
    if x == 3:
        pass
    else:
        print(f"x == {x}")

print(f"x finally equals to {x}")
print(f"sum finally equals to {sum}")
print("========================================================")


count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("The loop finished normally!")

for x in range(3):
    print(f"x = {x}")
else:
    print("x run finish")
