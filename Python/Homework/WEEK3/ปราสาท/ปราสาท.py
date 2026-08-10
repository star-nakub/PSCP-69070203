"""Tower"""
n = int(input())
row = 1
while row * row < n:
    row += 1
if n == 1:
    print(0)
elif n % 2 == 1:
    print(2 * row - 2)
else:
    print(2 * row - 3)
