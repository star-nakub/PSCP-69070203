"""name"""
def main():
    '''name'''
    #code
    ra = int(input())
    rb = int(input())
    st = str(input())
    ea = 1 / ((1 + (10 ** ((rb-ra)/400))))
    eb = 1 / ((1 + (10 ** ((ra-rb)/400))))
    if st == "A":
        print(f"{ea:.2f}")
    elif st == "B":
        print(f"{eb:.2f}")
    else:
        print("ERROR")
main()
