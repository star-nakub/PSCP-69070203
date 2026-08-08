"""Year"""
x = int(input())
if x < 1582:
    if not x % 4:
        print("yes")
    else:
        print("no")
else:
    if not x % 400:
        print("yes")
    elif not x % 100:
        print("no")
    elif not x % 4:
        print("yes")
    else:
        print("no")
