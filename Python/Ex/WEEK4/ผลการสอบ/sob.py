"""code"""
x = int(input())
y = int(input())
z = int(input())
if x >= 5 and y >= 20 and z >= 25:
    if x + y + z >= 50:
        print("pass")
    else:
        print("fail")
else:
    print("fail")
