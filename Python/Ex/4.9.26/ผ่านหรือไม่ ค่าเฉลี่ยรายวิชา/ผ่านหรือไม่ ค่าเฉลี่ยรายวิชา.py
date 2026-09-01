"""ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
x = int(input())
fail = False
add = 0
for _ in range(x):
    y = int(input())
    add += y
    if y < 50:
        fail = True
if add / x < 60:
    fail = True
print(f"{add/x:.1f}")
if fail:
    print("FAIL")
else:
    print("PASS")
