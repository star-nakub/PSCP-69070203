"""ผลรวมของค่าที่มากกว่า"""
x = int(input())
op = 0
add = 0
opp = ""
for _ in range(x):
    y = int(input())
    z = int(input())
    if y > z:
        op = y
    else:
        op = z
    if _ == x-1:
        add += op
        op = str(op)
        opp += op
        op = int(op)
        opp += " = "
        add = str(add)
        opp += (add)
    else:
        op = str(op)
        opp += op
        opp += " + "
        op = int(op)
        add += op
print(opp)
