import math

area = lambda r: math.pi * r * r
volume = lambda r, h: math.pi * r * r * h
print("{:6.2f}".format(area(2)))
print(volume(2, 5))
