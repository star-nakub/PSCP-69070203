"""ตั๋วหนังสุดป่วน"""
COUNT = int(input())
while COUNT > 0:
    try:
        x, y = map(int, input().split())
    except EOFError:
        break
    if x < 15:
        print(-1)
        continue
    if y > COUNT:
        print(-2)
        continue
    if x >= 60:
        NET = 150 * y * 0.5
    elif 15 <= x <= 22:
        NET = 150 * y * 0.8
    else:
        NET = 150 * y
    COUNT -= y
    print(f"{int(NET)} {COUNT}")
