def is_palindrome(teststr):
    teststr = teststr.lower()
    newStr = ''

    for c in teststr:
        if c.isalnum():
            newStr = newStr + c

    x = 0
    y = len(newStr) - 1
    while x < y:
        if newStr[x] != newStr[y]:
            return False
        x = x + 1
        y = y - 1
    return True

x = 0
y = 1
maxnum = x if (x>y) else y

print(maxnum)