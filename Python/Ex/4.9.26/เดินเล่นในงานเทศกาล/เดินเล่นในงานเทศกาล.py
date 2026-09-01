"""เดินเล่นในงานเทศกาล"""
x = input()
loop = len(x)
y = 0
z = 0
for i in range(loop):
    if x[i] == "N":
        y += 1
    elif x[i] == "S":
        y -= 1
    elif x[i] == "E":
        z += 1
    elif x[i] == "W":
        z -= 1
    rang  = abs(y) + abs(z)
print(f"{z} {y} {rang}")
