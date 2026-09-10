"""Arrow"""
x = input()
y = int(input())
z = len(x)
for k in range(z):
    if x[k] == "L":
        for i in range(y, 0, -1):
            print(" " * (i - 1) + "*" * i)
        for i in range(2, y + 1):
            print(" " * (i - 1) + "*" * i)
    elif x[k] == "R":
        for i in range(y):
            print(" " * (i * 2) + "*" * (y - i))
        for i in range(y - 2, -1, -1):
            print(" " * (i * 2) + "*" * (y - i))
    if k != len(x) - 1:
        print()
