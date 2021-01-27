def sum(n):
    # 嵌套函数,求阶乘n!
    def fact(a):
        t = 1
        for i in range(1, a + 1):
            t *= i
        return t

    s = 0
    for i in range(1, n + 1):
        s += fact(i)  # 调用嵌套函数fact(),求得1!+2!+...+n!的和
    return s


n = 6
print("{}以内阶乘之和为：{}".format(n, sum(n)))
