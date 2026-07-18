'''Saitama'''
import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
a1 = int(input())
b1 = int(input())
d1 = int(input())
c1 = int(input())
a2 = math.ceil(a / a1)
b2 = math.ceil(b / b1)
c2 = math.ceil(c / c1)
d2 = math.ceil(d / d1)
l = [a2, b2, c2, d2]
l.sort()
print(max(l))
