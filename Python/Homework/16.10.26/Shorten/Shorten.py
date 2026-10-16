"""Shorten"""
def main():
    """Shorten"""
    N = []
    Y = []
    while True:
        x = int(input())
        if x == -1:
            break
        N.append(x)
    if not len(N):
        pass
    else:
        e = 0
        start = N[0]
        stop = 0
        while e < len(N):
            if e == len(N)-1:
                stop = N[e]
                if start == stop:
                    Y.append(str(stop))
                else:
                    Y.append(f"{start}-{stop}")
            elif N[e]+1 == N[e+1]:
                pass
            else:
                stop = N[e]
                if start == stop:
                    Y.append(str(stop))
                else:
                    Y.append(f"{start}-{stop}")
                start = N[e+1]
            e += 1
        output = ""
        g = len(Y)
        for e in range(g):
            if not e:
                output += Y[e]
            else:
                output += ", "
                output += Y[e]
        print(output)
main()
