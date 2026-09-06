"""ThaiPlus"""
NAME = input()
AGE = int(input())
MON = int(input())
X = input()
FAM = int(input())
EXTRA = 0
if AGE < 18:
    RANK = "ERROR"
else:
    if X == "Y":
        RANK = "GOLD"
    elif MON <= 15000:
        RANK = "GOLD"
    elif 15000 < MON <= 30000:
        RANK = "SILVER"
    else:
        RANK = "ERROR"
    if RANK == "GOLD":
        EXTRA += 3000
        if FAM >= 3:
            EXTRA += 500
    elif RANK == "SILVER":
        EXTRA += 1500
        if FAM >= 3:
            EXTRA += 500
if RANK == "ERROR":
    print(f"{NAME} NOT ELIGIBLE")
else:
    print(f"{NAME} {RANK} {EXTRA}")
