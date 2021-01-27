from random import random  # random是Python内置模块
from random import *  # 导人random模块中的所有对象
from random import uniform as u

print(random())  # 返回0~1之间的随机小数
print(randint(10, 20))  # 返回两个整数之间的随机整数
print(uniform(5, 10))  # 返回两个数之间的随机实数
print(u(5, 10))
