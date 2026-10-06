"""LastStand"""
x = input()
L = [int(num) for num in x.strip("[]").split(",")]
for i in L:
    i = str(i)
    print(i[-1])
