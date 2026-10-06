"""Hint"""
def check(val, sym, end):
    """Hint"""
    val = int(val)
    end = int(end)
    if sym == "==":
        return val == end
    if sym == ">":
        return val > end
    if sym == "<":
        return val < end
    if sym == ">=":
        return val >= end
    if sym == "<=":
        return val <= end
    if sym == "!=":
        return val != end
    return False
x1, x2 = input().split()
y1, y2 = input().split()
z1, z2 = input().split()
for i in range(1000):
    i = f"{i:03d}"
    if (check(i[2], x1, x2) and check(i[1], y1, y2) and check(i[0], z1, z2)):
        print(i)
