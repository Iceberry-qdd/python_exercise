"""
itertools模块
迭代工具模块
"""
import itertools
# 产生ABCD的全排列
"""
iter1=itertools.permutations('ABCD')
for x in iter1:
    print(x)
"""
# 产生ABCDE的五选三组合
"""
iter2=itertools.combinations('ABCDE', 3)
for x in iter2:
    print(x)
"""
# 产生ABCD和123的笛卡尔积
"""
iter3=itertools.product('ABCD', '123')
for x in iter3:
    print(x)
"""
# 产生ABC的无限循环序列
iter4 = itertools.cycle(('A', 'B', 'C'))
for x in iter4:
    print(x)
