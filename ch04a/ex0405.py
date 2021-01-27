# program0307.py
print("类型：", type(range(1, 5)))
print(range.mro())

s = 0
for i in range(100):
    if i % 3 == 0:
        s += i
        print(i,end=',')
print('\n{}'.format(s))
