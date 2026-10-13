"""Bus Seat"""
x = int(input())
y = int(input())
z = int(input())
for i in range(x, 0, -1):
    for j in range(y):
        seat = j * x + i
        if seat == z:
            print("XX", end=" ")
        else:
            print(f"{seat:02d}", end=" ")
    print()
    if i % 2 == 1 and i != 1:
        print()
