'''
比较两个参数的大小
'''


def compare(arg1, arg2):
    result = arg1 > arg2
    return result  # 函数体内 result值


# 调用sum函数
btest = compare(10, 9.99)
print("函数的返回值:", btest)
