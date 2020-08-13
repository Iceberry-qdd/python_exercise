# 向列表中添加或移除元素
list1 = [1, 3, 5, 7, 100]
list1.append(200)  # 添加元素
print(list1)
list1.insert(2, 400)  # 添加元素,标识向2的位置插入一个值为400
print(list1)
list2 = [1000, 2000]
list1.extend(list2)  # 合并两个列表
print(list1)
list1 += list2  # 合并两个列表
print(list1)
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
    print(list1)
if 1234 in list1:
    list1.remove(1234)
print(list1)
# 删除指定索引的元素
list1.pop(0)
print(list1)
list1.pop(len(list1)-1)
print(list1)
list1.clear()  # 清空列表
print(list1)
