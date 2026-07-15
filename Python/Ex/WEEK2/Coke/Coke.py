"""coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
money = 0
caps = 0
count = 0
while count < d:
    if not b:
        money += a
        caps += 1
    elif caps >= b:
        money += c
        caps = caps - b + 1
    else:
        money += a
        caps += 1
    count += 1
print(money)
