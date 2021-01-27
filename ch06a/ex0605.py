def getscore(pe, eng, math, phy, chem):
    return pe * 0.5 + eng * 1 + math * 1.2 + phy * 1 + chem * 1


# getscore(93,89,78,89,72)    #按位置传递
value = getscore(pe=93, math=78, chem=72, eng=89, phy=89)  # 使用赋值参数
print(value)
