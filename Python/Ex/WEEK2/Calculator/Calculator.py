'''Cal'''
n = int(input())
if n == 1:
    print(n)
else:
    presses = n
    for i in range(1, n + 1):
        presses += len(str(i))
    print(presses)
