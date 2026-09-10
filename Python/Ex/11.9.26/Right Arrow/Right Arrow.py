"""Right Arrow"""
x = int(input())
y = int(input())
if y == 1:
    print("*"*x)
else:
    for i in range(y//2):
        print(" "*i,end="")
        print("*"*x)
    i += 1
    print(" "*i,end="")
    print("*"*x)
    for i in range(y//2-1,-1,-1):
        print(" "*i,end="")
        print("*"*x)
