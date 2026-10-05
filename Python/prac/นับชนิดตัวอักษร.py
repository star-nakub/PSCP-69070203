"""นับชนิดตัวอักษร"""
X = input().replace(" ",'')
UPP = 0
LOWW = 0
NUM = 0
for i in X:
    if i.isupper():
        UPP+=1
    elif i.islower():
        LOWW+=1
    elif i.isnumeric():
        NUM+=1
print(UPP,LOWW,NUM)
