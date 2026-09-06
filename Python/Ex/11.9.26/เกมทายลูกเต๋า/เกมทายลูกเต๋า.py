"""เกมทายลูกเต๋า"""
x = int(input())
y = int(input())
if 6 > x > 0 and x is y:
    print("Correct!")
elif 6 > x > 0 and x is not y:
    print("Wrong!")
else:
    print("Invalid")
