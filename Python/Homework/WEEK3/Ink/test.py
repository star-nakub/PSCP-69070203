"""INK"""
import math
S, N = map(int, input().split())
for _ in range(N):
    if not _ :
        pass
    X, Y = map(int,input().split())
    A = 3.1416 * (X**2 + Y**2) # pi*r^2 แทน r^2 == x^2+y^2
    T = math.ceil(A / S)
    print(T)
