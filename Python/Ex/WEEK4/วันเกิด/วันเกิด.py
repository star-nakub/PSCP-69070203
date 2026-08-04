"""BD"""
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
ya = y1-y2
ma = m1-m2
da = d1-d2
g = ya*365 + ma*30 + da
if y1 == y2 and m1 == m2 and abs(d1 - d2) <= 7:
    print(0)
elif 7 <= g <= -7:
    print(0)
elif (y1, m1, d1) < (y2, m2, d2):
    print(1)
else:
    print(2)
