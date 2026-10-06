"""ผลคูณเลขโดดที่ไม่เป็นศูนย์"""
x = input()
l = []
for i in x:
    if int(i):
        l.append(i)
if not l:
    ans = 0
else:
    ans = 1
for j in l:
    ans *= int(j)
print(ans)
