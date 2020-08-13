for i in range(100,1000):
    c = i % 10
    b = i // 10 % 10
    a = i // 100
    if c ** 3 + b ** 3 + a ** 3 == i:
        print(i,end=' ')