str1 = 'hello,world! '
print(len(str1))  # 计算长度
print(str1.capitalize())  # 首字母大写
print(str1.title())  # 每个单词首字母均大写
print(str1.upper())  # 所有字母均大写
print(str1.find('or'))  # 从字符串中查找子串所在位置
print(str1.find('shit'))  # 找不到返回-1
print(str1.index('or'))  # 从字符串中查找子串所在位置
# print(str1.index('shit'))#找不到发生异常
print(str1.startswith('He'))  # 检查字符串是否以指定的字符串开头
print(str1.startswith('hel'))  # 检查字符串是否以指定的字符串开头
print(str1.endswith('! '))  # 检查字符串是否以指定的字符串结尾
print(str1.center(50, '*'))  # 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.rjust(50, '*'))  # 将字符串以指定的宽度靠右放置左侧填充指定的字符

str2 = 'abc123456'
print(str2.isdigit())  # 检查字符串是否全由数字构成
print(str2.isalpha())  # 检查字符串是否以纯字母构成
print(str2.isalnum())  # 检查字符串是否仅由数字和字母构成

str3 = '  jackfrued@126.com '
print(str3)  # 原样输出
print(str3.strip())  # 修剪左右两侧空格之后输出
