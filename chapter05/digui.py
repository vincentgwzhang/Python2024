def sum(a):
    if a == 0 or a == 1:
        return a
    return sum(a-2) + sum(a-1)

print(sum(6))
# 0 1 1 2 3 5 8

