"""พิมพ์สัญลักษณ์"""
x = int(input())
for i in range(1,x+1):
    if not i % 5:
        print("X",end="")
    else:
        print("*",end="")
