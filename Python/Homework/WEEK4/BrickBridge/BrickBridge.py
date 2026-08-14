"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
big_used = min(b, goal // 5)
remains = goal - (big_used * 5)
if remains <= a:
    print(remains)
else:
    print("-1")
