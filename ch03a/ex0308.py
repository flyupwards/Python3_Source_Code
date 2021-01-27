print("aabbcc$123".isalnum())  # 因为存在$,返回Fa1se
print("hellos9".isalpha())  # 因为存在9,返回Fa1se
print("123".isdigit())
print("123".isnumeric())  # 识别全角数字
print("12二".isnumeric())  # 识别汉字数字
print("12二".isdigit())  # 不识别汉字是数字
print("ABc".isupper())
print("123".isdecimal())  # 只包含十进制字符
