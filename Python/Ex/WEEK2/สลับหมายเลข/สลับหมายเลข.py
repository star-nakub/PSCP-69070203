'''func'''
num = input()
sym = input()
rev = str(num[::-1])
rev = int(rev)
num = int(num)
ss = ''
if sym == "+":
    ss = num + rev
elif sym == "*":
    ss = num * rev
print(f"{num} {sym} {rev} = {ss}")
