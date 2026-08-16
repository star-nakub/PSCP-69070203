"""ชานมไข่มุก"""
FLAV, VOL = input().split()
TY, SWET, VOLC = input().split()
cal = 0
VOL = float(VOL)
VOLC = float(VOLC)
if FLAV == "H":
    cal += VOL*5
elif FLAV == "O":
    cal += VOL*3
elif FLAV == "J":
    cal += VOL*2
if TY == "R":
    if SWET == "1":
        cal += VOLC*12
    elif SWET == "2":
        cal += VOLC*18
    elif SWET == "3":
        cal += VOLC*25
if TY == "T":
    if SWET == "1":
        cal += VOLC*15
    elif SWET == "2":
        cal += VOLC*20
    elif SWET == "3":
        cal += VOLC*30
if TY == "M":
    if SWET == "1":
        cal += VOLC*10
    elif SWET == "2":
        cal += VOLC*15
    elif SWET == "3":
        cal += VOLC*20
if cal % 1:
    print(cal)
else:
    print(int(cal))
