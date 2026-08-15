"""carcc"""
Y = int(input())
CC = int(input())
if Y <= 1990:
    if CC <= 1500:
        print("1250")
    elif 1500 < CC <= 2000:
        print("1400")
    elif CC > 2000:
        print("2000")
elif 1991 <= Y <= 1999:
    if CC <= 1500:
        print("1100")
    elif 1500 < CC <= 2000:
        print("1300")
    elif CC > 2000:
        print("1700")
elif Y >= 2000:
    if CC <= 1500:
        print("1000")
    elif 1500 < CC <= 2000:
        print("1200")
    elif CC > 2000:
        print("1500")
