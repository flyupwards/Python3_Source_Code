op1 = 6
op2 = 2
print(~op1)  # 等价于二进制~00000110 = 11111001,输出-7
print(op1 | op2)  # 等价于二进制0110|0010=0110,输出6
print(op1 & op2)  # 等价于二进制0110&0010=0010,输出2
print(op1 >> op2)  # 0110右移2位为0001,输出1
print(op1 << op2)  # 0110左移2位为11000,输出24
