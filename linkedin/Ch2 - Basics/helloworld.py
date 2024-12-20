def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)


# 如果我直接运行这个 python 文件，那么 __name__ 就是 "__main__", 如果我是被人 import 进来的，那么 __name__ 就是这个 python 文件的文件名
#if __name__ == "__main__":
#    main()

print(__name__)