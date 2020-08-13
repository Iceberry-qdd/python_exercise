x = int(input('请输入一个整数：'))
y = 0
while x > 0:
    y = x % 10 + y * 10
    x = x // 10
print('反转后的数为：%d' % y)
