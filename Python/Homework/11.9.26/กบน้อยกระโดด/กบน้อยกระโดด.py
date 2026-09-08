"""กบน้อยกระโดด"""
x,y = map(int, input().split())
C = 0
if not (y-x)%2:
    while y > 1:
        C+=1
        y/=x
    print(C)
else:
    print("-1")
