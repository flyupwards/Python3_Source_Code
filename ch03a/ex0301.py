x = '\000\101\102'  # 八进制数表示的AscII码对应字符
print(x)
y = '\000\x61\x63'
print(y)
print(x, y)  # 运行结果的字符前有空格
print('Python\n语言\t程序\tDesign')
print("空字符NUL(null)：", '\000')
