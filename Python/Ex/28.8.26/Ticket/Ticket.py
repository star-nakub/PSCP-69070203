"""Ticket"""
x,y = map(str, input().split())
x = int(x)
mon = 0

if x < 5:
    mon = 0
elif 5 <= x <= 18:
    mon = 100
elif x >= 19:
    mon = 150
if y == "Wed" and x:
    mon /= 2
print(int(mon))
