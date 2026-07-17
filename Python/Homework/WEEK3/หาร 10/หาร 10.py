'''หาร 10'''
x = int(input())
for i in range(x+1,-1,-1):
    if not i % 10:
        print(i,end=" ")
