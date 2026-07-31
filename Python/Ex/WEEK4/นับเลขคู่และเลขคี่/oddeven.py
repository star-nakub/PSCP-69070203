"""odd"""
x = int(input())
y = int(input())
z = int(input())
odd = 0
even = 0
if x % 2:
    even += 1
else:
    odd += 1
if y % 2:
    even += 1
else:
    odd += 1
if z % 2:
    even += 1
else:
    odd += 1
print(odd)
print(even)
