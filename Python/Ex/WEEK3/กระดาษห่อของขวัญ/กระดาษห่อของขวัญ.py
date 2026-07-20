'''กระดาษห่อของขวัญ'''
def main():
    '''main'''
    pres = input().split(" ")
    r = float(pres[0])
    h = float(pres[1])
    g = float(pres[2])
    w = (2 * 3.14 * r) + g
    rh = (2*r) + h
    print(f"{rh:.2f} {w:.2f}")
main()
