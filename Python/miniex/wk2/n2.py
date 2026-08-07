"""dis"""
x = int(input())
y = int(input())
z = int(input())
long1 = abs(z-x)
long2 = abs(z-y)
if long1 < long2:
    print(f"Alice {long1}")
elif long1 > long2:
    print(f"Bob {long2}")
elif long1 == long2:
    print("Sundaes")
