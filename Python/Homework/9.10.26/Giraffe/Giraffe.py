"""Giraffe"""
x = int(input())
st = 0
z = -999
co = 0
for _ in range(x):
    y = int(input())
    if y < z and st == 1:
        co += 1
        st = 0
    elif y > z and st == 1:
        st = 1
    elif y > z:
        st += 1
    else:
        st = 0
    z = y
if st == 1:
    co += 1
print(co)
