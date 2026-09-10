"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
n = input().strip()
a = list(map(int, n))
if a[0] > 5:
    FLOOR = 9
elif a[1] > 5:
    FLOOR = 10
elif a[2] > 5:
    FLOOR = 11
elif a[3] > 5:
    FLOOR = 12
elif a[4] > 5:
    FLOOR = 14
else:
    FLOOR = 13
if n == n[::-1]:
    if a[0] + a[4] > 5:
        ROOM1 = 1
    elif a[1] * a[3] > 5:
        ROOM1 = 2
    else:
        ROOM1 = 0
else:
    if a[4] and round(a[0] / a[4]) > 5:
        ROOM1 = 1
    elif a[1] - a[4] > 5:
        ROOM1 = 2
    else:
        ROOM1 = 0
total = sum(a)
product = 1
for x in a:
    product *= x
if total > 25:
    ROOM2 = 1
elif product > 55:
    ROOM2 = 2
else:
    ROOM2 = 0
print(f"{FLOOR}{ROOM1}{ROOM2}")
