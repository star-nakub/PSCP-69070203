"""ระบบคิดคะแนนเกมออนไลน์"""
x = int(input())
y = int(input())
z = int(input())
score = x + y
if z > 3:
    score *= 1.5
if score >= 1500:
    CODE = 5
elif score >= 1000:
    CODE = 4
elif score >= 500:
    CODE = 3
elif score >= 200:
    CODE = 2
else:
    CODE = 1
if CODE == 5 and z >= 7:
    EXCODE = 99
elif CODE == 4 and y > 300:
    EXCODE = 88
else:
    EXCODE = 0
print(int(score))
print(CODE)
print(EXCODE)
