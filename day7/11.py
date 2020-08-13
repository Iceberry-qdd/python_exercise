# 使用元组
t1 = ('Iceberry', 38, True, '四川成都')
print(t1)
print(t1[0])  # 获取指定索引的元素
print(t1[3])
# 遍历
for member in t1:
    print(member, end=' ')
print()
'''
重新给元组赋值
元组是不可变类型，不能更新或者改变元组的元素。
通过现有字符串的片段在构造一个新的字符串的方式来等同于更新元组操作。
'''
# t1[0]='王大锤' # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t1 = ('王大锤', 20, True, '云南昆明')
print(t1)
# 将元组转换成列表
person = list(t1)
print(person)
# 列表可以修改
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
