"""infla"""
x = int(float(input()) * 100)
y = int(input())
Z = 381
for _ in range(y):
    x += (x * Z) // 10000
print(f"{x // 100}.{x % 100:02d}")
