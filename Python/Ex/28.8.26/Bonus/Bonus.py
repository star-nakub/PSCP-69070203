"""Bonus"""
x,y,z = map(str, input().split())
y = int(y)
z = int(z)
bonus = 0

if x == "M":
    bonus += 1500
elif x == "B":
    bonus += 1000
elif x == "G":
    bonus += 500

if x == "M" and y < 5:
    bonus += z*0.06
elif x == "B" and y < 5:
    bonus += z*0.05
elif x == "G" and y < 5:
    bonus += z*0.04

if x == "M" and 5 <= y <= 10:
    bonus += z*0.08
elif x == "B" and 5 <= y <= 10:
    bonus += z*0.06
elif x == "G" and 5 <= y <= 10:
    bonus += z*0.05

if x == "M" and y > 10:
    bonus += z*0.10
elif x == "B" and y > 10:
    bonus += z*0.07
elif x == "G" and y > 10:
    bonus += z*0.06

print(int(bonus))
