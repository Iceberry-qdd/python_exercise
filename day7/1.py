s1 = 'hello,world!'
s2 = "hello,world!"
s3 = """
hello,
world!
"""
print(s1, s2, s3, end='')

s4 = '\'hello,world!\''
s5 = '\n\\hello,world!\\\n'
print(s4, s5, end='')

s6 = '\141\142\143\x61\x62\x63'
s7 = '\u9b86\u660b'
print(s6, s7)

# 通过在字符串的最前面加上字母r来不希望字符串中的\表示转义
s8 = r'\'hello,world!\''
s9 = r'\n\\hello,world!\\\n'
print(s8, s9, end='')
