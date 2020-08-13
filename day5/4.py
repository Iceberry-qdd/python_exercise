count=2
a = 1
b = 1
print('%d %d' % (a,b),end = ' ')
while count < 20:
    a += b
    b += a
    print('%d' % a ,end = ' ')
    print('%d' % b ,end = ' ')
    count += 2