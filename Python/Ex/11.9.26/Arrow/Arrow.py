"""Arrow"""
x = input()
y = int(input())
if x == "L":
    for i in range(y,0,-1):
        print(" "*(i-1)+"*"*i)
    for i in range(2,y+1):
        print(" "*(i-1)+"*"*i)
if x == "R":
    for i in range(y):
        print(" "*(i*2)+"*"*(y-int(i)))
    for i in range(y-2,-1,-1):
        print(" "*(i*2),end="")
        print("*"*(y-i))
if x == "LR":
    for i in range(y,0,-1):
        print(" "*(i-1)+"*"*i)
    for i in range(2,y+1):
        print(" "*(i-1)+"*"*i)
    print()
    for i in range(y):
        print(" "*(i*2)+"*"*(y-int(i)))
    for i in range(y-2,-1,-1):
        print(" "*(i*2),end="")
        print("*"*(y-i))
if x == "RL":
    for i in range(y):
        print(" "*(i*2)+"*"*(y-int(i)))
    for i in range(y-2,-1,-1):
        print(" "*(i*2),end="")
        print("*"*(y-i))
    print()
    for i in range(y,0,-1):
        print(" "*(i-1)+"*"*i)
    for i in range(2,y+1):
        print(" "*(i-1)+"*"*i)
