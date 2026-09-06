"""PIZZA TIME"""
VISIT = int(input())
EATLEAST = int(input())
PIECES = int(input())
PIE = VISIT*EATLEAST
if PIE % PIECES:
    BOX = (PIE//PIECES)+1
else:
    BOX = PIE//PIECES
print(PIE)
print(BOX)
print((BOX*PIECES)-PIE)
