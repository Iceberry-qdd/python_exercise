"""
列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中
的一部分取出来创建出新的列表
"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
fruits2 = fruits[1:4]  # 列表切片
print(fruits2)
fruits3 = fruits[:]  # 复制列表
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
fruits5 = fruits[::-1]  # 倒转
print(fruits5)
