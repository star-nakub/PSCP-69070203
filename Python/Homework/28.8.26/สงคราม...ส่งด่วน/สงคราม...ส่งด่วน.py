"""สงคราม...ส่งด่วน"""
x,y = input().split()
z = float(input())
cost = 0
if x == "BKK":
    if y == "CNX":
        cost += 10
        cost += z*30
        print(f"{cost:.2f}")
    elif y == "PKT":
        cost += 25
        cost += z*50
        print(f"{cost:.2f}")
    else:
        print("Error")
elif x == "UBP":
    if y == "BKK":
        cost += 20
        cost += z*40
        print(f"{cost:.2f}")
    elif y == "PKT":
        cost += 40
        cost += z*70
        print(f"{cost:.2f}")
    else:
        print("Error")
elif x == "CNX":
    if y == "UBP":
        cost += 15
        cost += z*40
        print(f"{cost:.2f}")
    else:
        print("Error")
elif x == "PKT":
    if y == "CNX":
        cost += 30
        cost += z*60
        print(f"{cost:.2f}")
    else:
        print("Error")
else:
    print("Error")
