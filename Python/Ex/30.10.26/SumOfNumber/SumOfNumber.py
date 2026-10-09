"""SumOfNumber"""
x = int(input())
y = 0
z = x
while True:
    x = int(input())
    if x == -1:
        break
    y += x
    if y == z:
        break
print(y)
