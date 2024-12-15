try:
    n = int(input("try to input a num"))
    if n == 10:
        raise Exception("N can not be 10")
    n = n / 0
except ZeroDivisionError as e1:
    print("error 1", e1)
except: # 可以不声明exception, 可以声明，也可以声明后进一步 as e1
    print("error 2")
else:
    print("No error happened")
finally:
    print("I am here whatever")
