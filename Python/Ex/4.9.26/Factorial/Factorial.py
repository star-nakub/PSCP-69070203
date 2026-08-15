"""Factorial"""
x = int(input())
y = x
for i in range(x-1,1,-1):
    y*=i
print(y)
