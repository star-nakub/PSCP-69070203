'''high'''
x = int(input())
l = []
for _ in range(1,x+1):
    if not _ : # ไว้เกรียน PEP-8
        pass
    o = int(input())
    l.append(o)
    l.sort()
print(l[0])
