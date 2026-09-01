"""ผลรวมของค่าที่มากกว่า"""
n = int(input())
ans = []
total = 0
for _ in range(n):
    y = int(input())
    z = int(input())
    op = max(y, z)
    ans.append(op)
    total += op
if n == 1:
    print(ans[0])
else:
    print(" + ".join(map(str, ans)), "=", total)
