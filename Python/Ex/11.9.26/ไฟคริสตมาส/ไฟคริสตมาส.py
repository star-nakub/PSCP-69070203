"""ไฟคริสตมาส RGB"""
x,y = input().split()
y = int(y)
loop = y
if x == "R":
    for _ in range(loop):
        if loop > 0:
            print("Red",end=" ")
            loop -= 1
        if loop > 0:
            print("Green",end=" ")
            loop -= 1
        if loop > 0:
            print("Blue",end=" ")
            loop -= 1
if x == "G":
    for _ in range(loop):
        if loop > 0:
            print("Green",end=" ")
            loop -= 1
        if loop > 0:
            print("Blue",end=" ")
            loop -= 1
        if loop > 0:
            print("Red",end=" ")
            loop -= 1
if x == "B":
    for _ in range(loop):
        if loop > 0:
            print("Blue",end=" ")
            loop -= 1
        if loop > 0:
            print("Red",end=" ")
            loop -= 1
        if loop > 0:
            print("Green",end=" ")
            loop -= 1
