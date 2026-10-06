"""Left Arrow"""
x = int(input())
y = int(input())
for i in range(y//2,0,-1):
    print(" "*i,end="")
    print("*"*x)
print("*"*x)
for i in range(1,y//2+1):
    print(" "*i,end="")
    print("*"*x)
