def fact(n):
    t = 1
    for i in range(1, n + 1):
        t *= i
    return t


m2 = map(fact, (3, 4, 5, 6))
print(list(m2))
