"""infla"""
n = float(input())
k = int(input())
price = n
for i in range(k):
    increase = price * 0.0381
    increase = int(increase * 100) / 100
    price += increase
if n == 0:
    print(0)
else:
    print(f"{price:.2f}")
