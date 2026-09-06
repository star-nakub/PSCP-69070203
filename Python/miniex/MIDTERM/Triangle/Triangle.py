"""TriAngle"""
import math
A = int(input())
B = int(input())
C = int(input())
if A+B>C and A+C>B and B+C>A:
    if A == B and B == C:
        print("EQUILATERAL")
    elif math.sqrt((A**2+B**2)) == C or \
    math.sqrt((A**2+C**2)) == B or \
    math.sqrt((B**2+C**2)) == A:
        print("RIGHT TRIANGLE")
    elif A == B or B == C or A == C:
        print("ISOSCELES")
    elif B not in (A, C):
        print("SCALENE")
else:
    print("NOT A TRIANGLE")
