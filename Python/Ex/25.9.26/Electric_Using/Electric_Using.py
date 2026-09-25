"""Electric_Using"""
x = int(input())
FT = x * 0.5
PRICE = 0
if x > 200:
    PRICE += 1200
    PRICE += 500
    PRICE += 280
    PRICE += 50
    PRICE += (x - 200) * 15
elif x > 100:
    PRICE += 500
    PRICE += 280
    PRICE += 50
    PRICE += (x - 100) * 12
elif x > 50:
    PRICE += 280
    PRICE += 50
    PRICE += (x - 50) * 10
elif x > 10:
    PRICE += 50
    PRICE += (x - 10) * 7
elif x > 0:
    PRICE += x * 5
VAT = PRICE * 0.07
NET = PRICE+FT+VAT
print(f"{NET:.1f}")
