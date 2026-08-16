"""สามเหลี่ยม"""
x = int(input())
for i in range(1,x+1):
    if 2 < i < x:
        print("0"+"1"*(i-2)+"0")
    else:
        print("0"*i,end="\n")
    if i == x+1:
        print("0"*i,end="\n")
