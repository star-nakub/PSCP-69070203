"""temp"""
x = float(input())
y = input()
z = input()
c = 0
t = 0
if y == "C":
    c = x
elif y == "K":
    c = x - 273.15
elif y == "F":
    c = (x - 32) * 5 / 9
elif y == "R":
    c = x * 5 / 9 - 273.15
if z == "C":
    t = c
elif z == "K":
    t = c + 273.15
elif z == "F":
    t = (c * 9 / 5) + 32
elif z == "R":
    t = (c + 273.15) * 9 / 5
print(f"{t:.2f}")
