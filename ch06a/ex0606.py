a = 10  # 全局变量


def func(num):
    num += 1
    print("形参的值为：{}".format(num))
    print("形参的地址为：{}".format(id(num)))

    # 局部变量,只在函数内部有效
    a = 1
    # global a=31
    print(a, id(a))


func(a)
print(a, id(a))  # 函数调用后,变量a的值不发生变化
