def main():
    Y = []
    N = []
    row = int(input())
    colum = int(input())
    maximum = str(row * colum)
    seat = input().zfill(len(maximum))
    for i in range(row):
        for e in range(1,colum+1):
            N.append(str(row*e - i).zfill(len(maximum)))
        if seat in N:
            r = N.index(seat)
            N = N[:r] + ["X"*len(maximum)] + N[r+1:]
        Y.append(N)
        N = []
    j = len(Y)
    for e in range(j):
        output = Y[e][0]
        for l in Y[e]:
            if l == Y[e][0]:
                pass
            else:
                output += " "
                output += l
        print(output)
        if e%2 == 1 and e != j-1:
            print(" "*len(maximum)*colum + " "*(colum - 1))
main()