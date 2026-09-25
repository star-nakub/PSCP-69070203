"""แปลงดอกไม้"""
L, N = map(int, input().split())
PLANT = 0
STRIP = 0
while PLANT < N:
    STRIP += 1
    C = L * (2 * L * STRIP - L + 1) // 2
    PLANT += C
print(STRIP)
