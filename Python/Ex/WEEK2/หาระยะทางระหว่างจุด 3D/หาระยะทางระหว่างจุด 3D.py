'''3d'''
import math
txin = input().split(" ")
txin2 = input().split(" ")
x1 = int(txin[0])
y1 = int(txin[1])
z1 = int(txin[2])
x2 = int(txin2[0])
y2 = int(txin2[1])
z2 = int(txin2[2])
d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
print(f"{d:.2f}")
