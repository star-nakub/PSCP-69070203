"""fad"""
x = int(input())
ml = []
for i in range(x):
    my_list = list(map(int, input()))
    ml.extend(my_list)
    for o in range(0,len(ml)-1):
        ml[o] + ml[o+x]
if ml[o] == 9:
    print("YES")
print(len(ml))
print(my_list)
print(ml)
