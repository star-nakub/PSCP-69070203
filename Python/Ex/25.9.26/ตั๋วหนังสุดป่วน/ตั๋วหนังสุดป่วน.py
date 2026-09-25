"""ตั๋วหนังสุดป่วน"""
COUNT = int(input())
while COUNT > 0:
    PRICE = 150
    NET = 0
    x,y = map(int,input().split())
    COUNT -= y
    if COUNT < 0:
        print("-2")
        continue
    if x < 15:
        print("-1")
        COUNT += y
        continue
    if x >= 60 :
        NET += (PRICE*y)*0.5
    elif 22 >= x >= 15 and y > 2:
        NET += PRICE*y
        NET -= 150
    elif 22 >= x >= 15:
        NET += (PRICE*y)*0.8
    else:
        NET += PRICE*y
    NET = int(NET)
    print(f"{NET} {COUNT}")
