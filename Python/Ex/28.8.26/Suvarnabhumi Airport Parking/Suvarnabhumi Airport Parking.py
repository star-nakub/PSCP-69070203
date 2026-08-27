"""Suvarnabhumi Airport Parking"""
TIME1, TIME2 = map(int, input().split("."))
LEAVE1, LEAVE2 = map(int, input().split("."))
if not (0 <= TIME1 <= 23 and 0 <= TIME2 <= 59):
    print("ERROR")
elif not (0 <= LEAVE1 <= 23 and 0 <= LEAVE2 <= 59):
    print("ERROR")
else:
    enter = TIME1 * 60 + TIME2
    leave = LEAVE1 * 60 + LEAVE2
    t = leave - enter
    if t < 0 or t > 1440:
        print("ERROR")
    elif t <= 15:
        print("FREE")
    else:
        h = (t + 59) // 60
        if h == 1:
            print(25)
        elif h == 2:
            print(50)
        elif h == 3:
            print(80)
        elif h == 4:
            print(110)
        elif h == 5:
            print(145)
        elif h == 6:
            print(180)
        else:
            print(250)
