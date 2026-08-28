"""ของขวัญและขโมย"""
X, Y, Z = map(int, input().split())
L = []
CURR = 1
TIME = 0
for _ in range(1,X+1):
    L.append(_)
for _ in range(1,X+1):
    CURR += Y
    TIME += 1
    print(CURR)
    if CURR > X:
        CURR -= X
    # if L[CURR] == Z:
    #     print(TIME)

    # if CURR > X:
    #     CURR -= X
    # if L[CURR-1] == Z or not L[CURR-1]:
    #     print(_+1)
    #     break