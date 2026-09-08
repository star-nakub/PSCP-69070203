"""ไพ่ 44 ใบ"""
card = input().upper()
x = card[:-1]
y = card[-1]
if x == "A":
    x = "ace"
elif x == "J":
    x = "jack"
elif x == "Q":
    x = "queen"
elif x == "K":
    x = "king"
if y == "D":
    y = "diamonds"
elif y == "H":
    y = "hearts"
elif y == "S":
    y = "spades"
elif y == "C":
    y = "clubs"
print(x, "of", y)
