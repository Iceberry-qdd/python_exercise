x=int(input('请输入第一个正整数：'))
y=int(input('请输入第二个正整数：'))
if x > y:
    x,y=y,x
for i in range(x,0,-1):
    if x % i ==0 and y % i ==0:
        print('%d和%d的最大公约数为%d' % (x,y,i))
        print('%d和%d的最小公倍数为%d' % (x,y,x*y//i))
        break    