"""Elon Musk (X-shape)"""
x, k = input().split()
x = int(x)
mid = x // 2
for i in range(x):
    for j in range(x):
        if j in (i, x - 1 - i):
            if k == '#':
                print('#', end='')
            else:
                distance = abs(i - mid)
                print(chr(ord(k) + distance), end='')
        else:
            print('-', end='')
    print()
