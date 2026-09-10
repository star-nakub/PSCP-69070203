x,y = input().split()
x=int(x)
mid = x//2
for i in range(x):
    for j in range(x):
        if y == "#":
            if i == j or j == x - 1 - i:
                print("#",end="")
            else:
                print("-",end="")
        else:
            if i == j or j == x - 1 - i:
                let = ord(y)
                print(chr(let+abs(i-mid)),end="")
            else:
                print("-",end="")
    print()