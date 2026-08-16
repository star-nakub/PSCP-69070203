"""สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP
vip = input()
x = int(input())
total = Decimal("0")
for i in range(x):
    if i:
        pass
    y = Decimal(input())
    total += y
if vip == "Y":
    net = total * Decimal("0.95")
elif total >= 500:
    net = total * Decimal("0.97")
else:
    net = total
net = net.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(f"{net:.2f}")
