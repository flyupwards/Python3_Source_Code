# 计算序列中的奇数,保存到参数ls中
tup = (1, 5, 7, 8, 12, 9)
ls = []


def getodd(tup1, ls1):  # 参数为组合数据类型
    for i in tup1:
        if i % 2:
            ls1.append(i)
    print(ls1)
    print(id(ls1))
    return ls1


getodd(tup, ls)  # 函数调用前后,1s的值发生了变化,但id值不变
print(ls)
print(id(ls))
