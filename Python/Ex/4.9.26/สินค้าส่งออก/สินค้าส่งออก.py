"""สินค้าส่งออก"""
x = int(input())
add = 0
even = 0
odd = 0
for _ in range(x):
    y = int(input())
    add += y
    if not y % 2:
        even += 1
    else:
        odd += 1
print(f"SUM {add}\nEVEN {even}\nODD {odd}")
