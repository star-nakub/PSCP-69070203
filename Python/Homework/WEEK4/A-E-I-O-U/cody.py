"""aeiou"""
x = input().lower()
a=0
e=0
i=0
o=0
u=0
sara = ["a","e","i","o","u"]
for char in x:
    if char == "a":
        a += 1
    elif char == "e":
        e += 1
    elif char == "i":
        i += 1
    elif char == "o":
        o += 1
    elif char == "u":
        u += 1
if sara[0] in x:
    print(f"a : {a}")
if sara[1] in x:
    print(f"e : {e}")
if sara[2] in x:
    print(f"i : {i}")
if sara[3] in x:
    print(f"o : {o}")
if sara[4] in x:
    print(f"u : {u}")
