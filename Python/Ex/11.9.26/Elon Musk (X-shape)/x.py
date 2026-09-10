x,y = input().split()
x = int(x)
mid = x//2
for i in range(x):
    for j in range(x):
        if y == "#":
            if i == j or i == x - 1 - j:
                print("#",end="")
            else:
                print("-",end="")
        else:
            if i == j or i == x - 1 - j:
                distance = abs(i - mid)
                print(chr(ord(y) + distance), end='')
            else:
                print("-",end="")
    print()
