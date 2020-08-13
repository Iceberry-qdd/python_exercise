# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)  # 集合里的元素不允许重复
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和从集合删除元素
set1.add(4)
set1.add(5)  # 只能一个一个添加
print(f'After set1 added:{set1}')
set2.update([11, 12])  # 添加多个元素
print(f'After set2 updated:{set2}')
set2.discard(5)  # 查找并删除元素5(如果存在)(若不存在，则忽略)
print(f'After set2 discarded:{set2}')
if 4 in set2:
    set2.remove(4)  # 删除元素4(如果存在)(若不存在，则报错)
print(f'After set2 removed:{set2}')
print(set3.pop())  # 删除第一个元素
print(set3)

# 集合的成员、交集、并集、差集等运算
print('\n集合的成员、交集、并集、差集等运算:')
print(f'set1:{set1}')
print(f'set2:{set2}\n')

print(f'set1 & set2:{set1&set2}')  # 交集
print(f'set1 intersection set2:{set1.intersection(set2)}')  # 交集

print(f'set1 | set2:{set1|set2}')  # 并集
print(f'set1 union set2:{set1.union(set2)}')  # 并集

print(f'set1 - set2:{set1-set2}')  # 差集
print(f'set1 difference set2:{set1.difference(set2)}')  # 差集
print(f'set2 - set1:{set2-set1}')  # 差集
print(f'set2 difference set1:{set2.difference(set1)}')  # 差集

print(f'set1 ^ set2:{set1^set2}')  # 对称差集
# 对称差集
print(f'set1 symmetric_difference set2:{set1.symmetric_difference(set2)}')

# 判断子集和超集
print('\n判断子集和超集:')
set1.discard(4)
set1.discard(5)
print(f'set1:{set1}')
print(f'set2:{set2}\n')

print(f'set2 <= set1:{set2<=set1}')  # 判断子集
print(f'set2 issubset set1:{set2.issubset(set1)}')  # 判断子集
print(f'set1 <= set2:{set1<=set2}')  # 判断子集
print(f'set1 issubset set2:{set1.issubset(set2)}')  # 判断子集

print(f'set2 >= set1:{set2>=set1}')  # 判断超集
print(f'set2 issuperset set1:{set2.issuperset(set1)}')  # 判断超集
print(f'set1 >= set2:{set1>=set2}')  # 判断超集
print(f'set1 issuperset set2:{set1.issuperset(set2)}')  # 判断超集
