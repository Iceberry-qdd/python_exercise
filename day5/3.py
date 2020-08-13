for i in range(100 // 5):
    for j in range(100 // 3):
        k = 100 - i - j
        if i * 5 + j * 3 + k / 1 == 100:
            print('公鸡：%d，母鸡：%d，小鸡：%d' % (i,j,k))