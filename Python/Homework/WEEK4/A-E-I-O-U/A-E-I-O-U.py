"""aeiou"""
x = input().lower()
a=0
e=0
i=0
o=0
u=0
le = len(x)
sara = ["a","e","i","o","u"]
for _ in le:
    if x[_] == "a":
        a+=1
    elif x[_] == "e":
        e+=1
    elif x[_] == "i":
        i+=1
    elif x[_] == "o":
        o+=1
    elif x[_] == "u":
        u+=1
if sara[0] in xl:
    print(f"a : {a}")
if sara[1] in xl:
    print(f"e : {e}")
if sara[2] in xl:
    print(f"i : {i}")
if sara[3] in xl:
    print(f"o : {o}")
if sara[4] in xl:
    print(f"u : {u}")
