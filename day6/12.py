def foo():
    # b为局部变量
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar()


if __name__ == '__main__':
    # a为全局变量
    a = 100
    foo()
