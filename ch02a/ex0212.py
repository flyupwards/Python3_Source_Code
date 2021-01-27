x = 10
y = 20
m = 3.0
n = 8.2
b = x + y > x - y * -1 and m < n % 3
# print("x+y>x-y*-1为{}".format(x+y>x-y*-1))
# print("m<n%3为{}".format(m<n%3))
print(b)
b1 = ((x + y) > (x - y * (-1))) and m < (n % 3)
print(b1)
b2 = ((x + y) > (x - y * (-1))) and (m < (n % 3))
print(b2)
