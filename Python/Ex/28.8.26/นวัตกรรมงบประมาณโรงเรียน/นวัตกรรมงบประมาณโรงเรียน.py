"""นวัตกรรมงบประมาณโรงเรียน"""
name = input()
f1 = name[0].upper()
l1 = name[-1].upper()
fac = ord(f1)
lac = ord(l1)
num = []
for i in range(10):
    if (i + 1) % 2 == 1:
        num.append(fac + i)
    else:
        num.append(lac - i)
long = len(name)
for i in range(10):
    num[i] %= long
    if num[i] > 9:
        num[i] %= 10
for x in num[2:8]:
    print(x, end=" ")
