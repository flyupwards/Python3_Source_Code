from functools import reduce

r1 = reduce(lambda x, y: x + y, (1, 2, 3, 4, 5))
print(r1)

# reduced()函数的第3个参数设置初值10000
r2 = reduce(lambda x, y: x + y, (1, 2, 3, 4, 5), 10000)
print(r2)

# 基于整数列表生成整数数值
r3 = reduce(lambda x, y: x * 10 + y, [1, 2, 3, 4, 5])
print(r3)
