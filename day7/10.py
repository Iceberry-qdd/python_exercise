#关于yield：https://blog.csdn.net/mieleizhi0522/article/details/82142856/
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a


def main():
    for val in fib(20):
        print(val, end=' ')


if __name__ == '__main__':
    main()
