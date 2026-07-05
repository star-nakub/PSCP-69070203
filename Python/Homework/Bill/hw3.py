"""bill"""
def main():
    '''bill'''
    #code
    mon = int(input())
    sc = mon * 10/100
    if sc <= 50:
        sc = 50
    elif sc >= 1000:
        sc = 1000
    net = (mon + sc) * 1.07
    print(f"{net:.2f}")
main()
