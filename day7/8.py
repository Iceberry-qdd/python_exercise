# 列表排序
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)  # 按每个元素首字母正序
print(list2)
list3 = sorted(list1, reverse=True)  # 按每个元素首字母倒序
print(list3)
list4 = sorted(list1, key=len)  # 按字符串长度从短到长排序
print(list4)
list4 = sorted(list1, reverse=True, key=len)  # 按字符串长度从短到长排序
print(list4)
list1.sort(reverse=True)  # 直接对list1排序
print(list1)
