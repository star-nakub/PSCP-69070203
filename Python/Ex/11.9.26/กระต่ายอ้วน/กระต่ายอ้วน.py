"""กระต่ายอ้วน"""
x = int(input())
FAT = -999999999999999999
OVW = 0
NAMEFAT = ""
for _ in range(x):
    y,z = input().split()
    z = int(z)
    FAT = int(FAT)
    if z > FAT:
        FAT = z
        NAMEFAT = y
    if z > 15:
        OVW += 1
print(OVW)
print(NAMEFAT)
