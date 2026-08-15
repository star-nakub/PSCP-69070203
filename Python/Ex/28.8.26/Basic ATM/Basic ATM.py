"""Basic ATM"""
x = int(input())
thou = x // 1000
fhun = (x%1000) // 500
hun = (x%500) // 100
if not x%100:
    if thou > 0:
        print("1000 =", thou)
    if fhun > 0:
        print("500 =", fhun)
    if hun > 0:
        print("100 =", hun)
else:
    print("ERROR")
