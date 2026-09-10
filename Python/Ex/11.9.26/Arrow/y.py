direction = input()
n = int(input())

if direction == "R":
    # ขาลง
    for i in range(n):
        print(" " * (2 * i) + "*" * (n - i))

    # ขาขึ้น
    for i in range(n - 2, -1, -1):
        print(" " * (2 * i) + "*" * (n - i))

elif direction == "L":
    # ขาลง
    for i in range(n):
        print(" " * (n - 1 - i) + "*" * (n - i))

    # ขาขึ้น
    for i in range(n - 2, -1, -1):
        print(" " * (n - 1 - i) + "*" * (n - i))
