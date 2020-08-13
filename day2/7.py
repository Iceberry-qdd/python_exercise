year = int(input("请输入要判断的年份："))
is_leap = year % 4 == 0 and year % 100 !=0 or year % 400 == 0
print("%d年是否为闰年：" % year,is_leap)