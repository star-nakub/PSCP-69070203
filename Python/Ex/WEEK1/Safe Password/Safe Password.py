"""code"""
C = str(input())
code = int(input())
if C == "H" and code == 4567:
    print("safe unlocked")
elif C == "H":
    print("safe locked - change digit")
elif code == 4567:
    print("safe locked - change char")
else:
    print("safe locked")
