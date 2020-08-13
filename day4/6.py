x = int(input('请输入一个正整数：'))
flag=True
if x == 1:
    print('1既不是素数，也不是合数')
    flag=False
elif x == 2:
    flag=True
else:
    for i in range(2,x):
        if x%i == 0:
            print('%d是合数' % x)
            flag = False
            break
        else:
            #flag = True
            continue
if flag == True:
    print('%d是素数' % x)