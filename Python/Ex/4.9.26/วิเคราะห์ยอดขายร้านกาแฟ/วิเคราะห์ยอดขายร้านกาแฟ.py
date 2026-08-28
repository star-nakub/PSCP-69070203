"""วิเคราะห์ยอดขายร้านกาแฟ"""
X = int(input())
L = []
ALL = 0
for _ in range(X):
    Y = int(input())
    ALL += Y
    L.append(Y)
    L.sort()
print(ALL)
print(L[-1])
print(L[0])
print(f"{ALL/X:.1f}")
