# ex0408-2.py

k = eval(input("请输入计算阶乘的数值:"))
print(k)
sum1 = 0
t = 1
for i in range(1, k + 1):
    t *= i
    sum1 += t
print("1!+2!+…+{0}!={1}".format(k, sum1))
