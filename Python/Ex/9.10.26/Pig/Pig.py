"""Pig"""
x = int(input())
l = list(map(int,input().split()))
val = 0
ans = ""
if x == 1:
    print(max(l))
else:
    for i in range(0,x*2-1,2):
        val += max(l[i],l[i+1])
        ans += str(max(l[i],l[i+1])) + " + "
    ans = ans.rstrip("+ ")
    ans += " = " + str(val)
    print(ans)
