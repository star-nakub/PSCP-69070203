"""กบน้อยกระโดด"""
STEP,FINAL = map(int, input().split())
CURR = 0
JUMP = 0
while FINAL > 0:
    FINAL -= STEP
    STEP -= 2
    JUMP += 1
    if STEP < 0:
        break
if CURR >= FINAL:
    print(JUMP)
else:
    print("-1")
