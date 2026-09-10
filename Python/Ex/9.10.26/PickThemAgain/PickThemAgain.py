"""PickThemAgain"""
x = list(map(int,input().split()))
yes = 0
for i in range(len(x) - 1, -1, -1):
    if not x[i] % 3 or not x[i] % 5:
        print(x[i])
        yes = 1
if not yes:
    print("Nope")
