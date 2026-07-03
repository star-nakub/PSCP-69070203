"""bill"""
def main():
    '''bill'''
    mon = int(input())

    sc = mon * 10 / 100
    vat = mon * 7 / 100

    if sc <= 50:
        sc = 50
    elif sc >= 1000:
        sc = 1000

    net = mon + sc + vat

    print(f"{net:.2f}")
    print(f"{sc:.2f}")

main()