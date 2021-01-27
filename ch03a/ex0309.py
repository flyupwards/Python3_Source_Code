str1 = "hi,Python!hi,Java!"
print(str1)
print(str1.startswith("hi", 3, 9))

print(str1.endswith("Java!"))
print(str1.startswith("hi", 3))  # 从str1的第3个字符开始判断,不以"hi"开头
print(str1.endswith("hi", 3, 12))  # 判断str1的第3~12个字符,以"hi"结尾
