lst1 = [3, 5, -4, -1, 0, -2, -6]


# lst2 = sorted(lst1, key=lambda x: abs(x))

def get_abs(x):
    return abs(x)


lst2 = sorted(lst1, key=get_abs)

print(type(lst2))
print(lst2)
