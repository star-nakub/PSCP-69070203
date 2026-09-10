"""ใส่กล่อง"""
a, b, c, d = map(int, input().split())
lowest = float("inf")
for A in range(c, d + 1):
    waste = (a % A) * (b % A)
    if waste < lowest:
        lowest = waste
print(lowest)
