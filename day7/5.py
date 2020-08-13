# 遍历列表
list1 = [1, 3, 5, 7, 100]
print(list1)
list2 = ['hello']*3  # 乘号表示列表元素的重复
print(list2)
print(len(list1))  # 计算列表长度(元素个数)
# 下标(索引)运算
print(list1[0])
print(list1[4])
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 取倒数第1号元素
print(list1[-3])  # 取倒数第3号元素
list1[2] = 300
print(list1)
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index], end=' ')
print()
# 通过for循环遍历列表元素
for elem in list1:
    print(elem, end=' ')
    print()
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(f'{index}-{elem}', end=' ')
print()
