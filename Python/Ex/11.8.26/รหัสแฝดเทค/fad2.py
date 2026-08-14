"""fad"""
lak = int(input())
ra1 = input()
ra2 = input()
x = 0
for i in range(lak):
    if int(ra1[i]) + int(ra2[i]) != 9:
        x += 1
if not x:
    print("YES")
else:
    print(f"NO {x}")
