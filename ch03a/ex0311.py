str1 = "hi, Python, hi, Java!"
print(str1)

print(str1.split())  # 默认使用空格做分配符,str1中无空格,列表中只有一个元素

print(str1.split(","))  # 使用逗号做分配符,3个逗号,分隔3次

print(str1)
print(str1.split(",", 2))  # 使用逗号做分配符,限制分隔2次

lst = ['sfg', ' Python', 'hsfgi', 'Java! ']
s = ''  # 空字符
s2 = ' '  # 空格
print(lst)
print(s.join(lst))  # 将列表连接为字符串
print(s2.join(lst))

str1 = " hi, Python, hi, Java! "
print(str1.lstrip())
print(str1.rstrip())
