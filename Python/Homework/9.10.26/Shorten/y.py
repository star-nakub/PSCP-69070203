"""Shorten"""
l = []
while True:
    n = int(input())
    if n == -1:
        break
    l.append(n)
result = []
start = l[0]
prev = l[0]
for n in l[1:]:
    if n == prev + 1:
        prev = n
    else:
        if start == prev:
            result.append(str(start))
        else:
            result.append(f"{start}-{prev}")
        start = n
        prev = n
if start == prev:
    result.append(str(start))
else:
    result.append(f"{start}-{prev}")
print(", ".join(result))
