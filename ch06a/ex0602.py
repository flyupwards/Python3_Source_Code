'''
计算圆的面积s
'''


def getcirclearea(r):
    print("圆的面积s={:8.2f}".format(3.14 * r * r))
    return


getcirclearea(3)

getcirclearea  # 函数名变量在内存中的地址

print(getcirclearea(3))  # return语句无返回值时,返回None
