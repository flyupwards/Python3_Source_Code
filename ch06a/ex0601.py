# 函数的定义
def hello():
    print("Hello Python")


def getarea(x, y):
    '''
    参数为两个数值数据,或者一个字符串和一个整数。
    '''
    print("{}*{}={}".format(x, y, x * y))
    return x * y


# 函数的调用
hello()

# getarea(3.0,2.0)
getarea("hello", 2)
