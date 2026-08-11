"""Tower"""
N = int(input())
if N**0.5 == int(N**0.5): # หาแถว
    cur = int((N**0.5) - 1)
else:
    cur = int(N**0.5) # สามเหลี่ยมคว่ำกับหงาย
if N % 2 == cur % 2 :
    print(2 * cur - 1)
else:
    print(2 * cur)
