s = all([1, 2])  # 列表中每个元素逻辑值均为True,返回True
# s = all([0, 1, 2])  # 列表中元素0的逻辑值为False,返回False
# s = all(())  # 空元组
# s = all({})  # 空字典
# s = any([0, 1, 2])  # 列表元素有一个为rue.则返回True
# s = any([0, 0])  # 列表元素全部为False,则返回 False
# s = any([])  # 空列表
print(s)
