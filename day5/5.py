sum = 1
for num in range(2,10000):
    for i in range(2,num+1):
        if num % i == 0:
            sum += i
    if sum == 2 * num:
        print(num,end=' ')
    sum = 1