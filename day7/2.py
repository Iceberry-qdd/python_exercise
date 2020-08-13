s1 = 'hello'*3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # 左闭右开
print(str2[2:])  # 从2开始到结尾
print(str2[2::2])  # 从2开始步幅为2
print(str2[::2])  # 从一开始步幅为2
print(str2[::-1])  # 倒转
print(str2[-3:-1])  # 从下表倒数第3到倒数第1，左开右闭
