print(r'\n')

print('a\nc')

print(b'123')

print(bin(8))
print(bin(123).replace("0b", ""))

a = "Hello"
b = " Python"
print(a + b)
print(a * 2)
print(a[1])
print(a[1:4])
print('H' in a)
print('M' not in a)
print(r'\n')

str1 = "Hi,Python!"
# str1重复显示两次，str1未发生变化
print(str1 * 2)

# 测试str1在内存中的标识
print(id(str1), str1)

# str1连接字符串
str1 += "Hi, Java!"
print(str1)

# id发生改变
print(id(str1), str1)
# print(str1)

# 字符串切片操作
print(str1, str1[3:9])

print(str1, str1[-7:-3])  # 从后向前切片,最后一个字符索引是-1

print(str1, str1[:-6])  # 从索引为-6的字符到字符串首

# 字符串中包含给定字符的测试
print("java" in str1)
print("Java" in str1)
