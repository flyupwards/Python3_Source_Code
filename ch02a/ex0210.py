x = 5  # 为一个变量赋值,x值为5
x = x + 1  # 进行赋值运算,x值最后为6
x = y = z = 5  # 为多个变量赋一个值，x、y、z值均为5
x, y, z = 3, 4, 5  # 为多个变量赋多个值,x值为3,y值为4,z值为5
print(x)

x = 5
y = 3
x += y
print(x, y)
x -= y
print(x, y)
x /= y
print(x, y)
