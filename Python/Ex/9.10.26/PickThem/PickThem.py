"""PickThem"""
import json
x = input()
nop = 0
ans = json.loads(x)
for i in ans:
    if not i % 2:
        print(i)
        nop += 1
if not nop:
    print("Nope")
