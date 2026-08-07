"""sara"""
n = int(input())
vow = []
x = 0
sara = ["A","E","I","O","U"]
for i in range(1,n+1):
    y = input()
    vow.append(y)
    if y in sara:
        x+=1
print(x)
if "A" in vow and "E" in vow and "I" in vow and "O" in vow and "U" in vow:
    print("YES")
else:
    print("NO")
