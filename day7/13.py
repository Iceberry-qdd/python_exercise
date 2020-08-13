# 创建字典的字面量语法
scores = {'Iceberry': 95, 'Ben': 78, 'Alice': 82}
print(scores)
# 创建字典的构造器语法
item1 = dict(one=1, two=2, three=3, four=4)
print(item1)
# 通过zip函数将两个序列压成字典
item2 = dict(zip(['a', 'b', 'c'], '123'))
print(item2)
# 创建字典的推导式语法
item3 = {num: num**2 for num in range(1, 10)}
print(item3)

# 通过键可以获取字典中对应的值
print(scores['Iceberry'])
print(scores['Alice'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}:{scores[key]}')

# 更新字典中的元素
scores['Ben'] = 65  # 修改
scores['诸葛王朗'] = 71  # 增加
scores.update(冷面=57, 方启鹤=85, Iceberry=100)  # 增加/修改
print(scores)

# 查找元素
if 'Alice' in scores:
    print(scores['Alice'])
    print(scores.get('Alice'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))  # 若存在，获取值，默认值无效；若不存在，则新增，并设为默认值

# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('Iceberry', 10))  # 默认值

# 清空字典
scores.clear()
print(scores)
