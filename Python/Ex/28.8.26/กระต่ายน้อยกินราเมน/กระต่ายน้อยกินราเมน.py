"""กระต่ายน้อยกินราเมน"""
price = {('S', 'R'): 60, ('S', 'T'): 80,
    ('M', 'R'): 80, ('M', 'T'): 100,
    ('L', 'R'): 100, ('L', 'T'): 120}
size, type1 = input().split()
total = price[(size, type1)]
face = input().split()
if face[0] != 'N':
    type2 = face[0]
    C1 = int(face[1])
    if type2 == 'P':
        total += 15 * C1
    elif type2 == 'E':
        total += 10 * C1
print(total)
