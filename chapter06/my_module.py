def add1(a, b):
    return a + b


def total2(a):
    '''
    参数a 是接受一个列表
    return: a列表中每个元素的平方和
    '''
    result = 0
    for val in a:
        result += val ** 2
    return result


name = 'vincent'

def printName():
    print(name)
