"""taxi"""
x = int(input())
if x == 1 :
    print("35")
elif 1 < x <= 10:
    print(35+((x-1)*5))
elif x > 10:
    print(80+(x-10)*8)
elif not x:
    print("0")
