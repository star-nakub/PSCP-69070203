"""Bonus"""
x, y, z = input().split()
y = int(y)
z = float(z)

bonus = 0

if x == "M":
    bonus += 1500
elif x == "B":
    bonus += 1000
elif x == "G":
    bonus += 500

if y <= 5:
    if x == "M":
        bonus += z * 0.06
    elif x == "B":
        bonus += z * 0.05
    elif x == "G":
        bonus += z * 0.04

elif y <= 10:
    if x == "M":
        bonus += z * 0.08
    elif x == "B":
        bonus += z * 0.06
    elif x == "G":
        bonus += z * 0.05

else:
    if x == "M":
        bonus += z * 0.10
    elif x == "B":
        bonus += z * 0.07
    elif x == "G":
        bonus += z * 0.06

print(int(bonus))
