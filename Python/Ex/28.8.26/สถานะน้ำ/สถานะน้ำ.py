"""สถานะน้ำ"""
X = int(input())
Y = input().lower()
if Y == "c":
    if X <= 0:
        print("solid")
    elif 0 < X < 100:
        print("liquid")
    elif X >= 100:
        print("gas")
elif Y == "f":
    if X <= 32:
        print("solid")
    elif 32 < X < 212:
        print("liquid")
    elif X >= 212:
        print("gas")
