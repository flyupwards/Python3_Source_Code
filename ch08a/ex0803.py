import sys
import mymodule  # 导入模块,mymodule中的导入语句被执行
import mymodule

sys.path.append('./')  # 在Python标准库中修改site.py文件，并编辑sys.path
print(sys.path)
print(mymodule.x)
mymodule.testm()
mymodule.x = 100
print(mymodule.x)
help(mymodule)  # 查看模块信息
dir(mymodule)  # 列出模块的属性列表，以"__"开头和结尾的是 Python的内置属性,其他为模块中的变量名
temp = mymodule
print(temp.x)
temp.testm()
