# ex0409.py

k = eval(input("请输入计算阶乘的数值： "))
print(k)
sum1 = 0
i = 1
while i <= k:
    t = j = 1
    while j <= i:
        t *= j
        j += 1
    sum1 += t
    i += 1
print("1!+2!+…+{0}!={1}".format(k, sum1))
