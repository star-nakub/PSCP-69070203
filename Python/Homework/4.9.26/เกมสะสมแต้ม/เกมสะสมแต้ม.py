"""เกมสะสมแต้ม"""
X = int(input())
SCORE = 0
for i in range(X):
    if i:
        pass
    Y = input()
    if Y == "+":
        SCORE += 10
    elif Y == "-":
        SCORE -= 5
print(SCORE)
