"""Units"""
X = float(input())
U2 = input()
U1 = input()
if U1 == U2:
    print(f"{X:.4f}")
elif U1 == "NIU" and U2 == "KUEP":
    X/=12
    print(f"{X:.4f}")
elif U1 == "NIU" and U2 == "SOK":
    X/=12
    X/=2
    print(f"{X:.4f}")
elif U1 == "NIU" and U2 == "WA":
    X/=12
    X/=2
    X/=4
    print(f"{X:.4f}")
elif U1 == "NIU" and U2 == "SEN":
    X/=12
    X/=2
    X/=4
    X/=20
    print(f"{X:.4f}")
elif U1 == "KUEP" and U2 == "NIU":
    X*=12
    print(f"{X:.4f}")
elif U1 == "KUEP" and U2 == "SOK":
    X/=2
    print(f"{X:.4f}")
elif U1 == "KUEP" and U2 == "WA":
    X/=2
    X/=4
    print(f"{X:.4f}")
elif U1 == "KUEP" and U2 == "SEN":
    X/=2
    X/=4
    X/=20
    print(f"{X:.4f}")
elif U1 == "SOK" and U2 == "NIU":
    X*=12
    X*=2
    print(f"{X:.4f}")
elif U1 == "SOK" and U2 == "KUEP":
    X*=2
    print(f"{X:.4f}")
elif U1 == "SOK" and U2 == "WA":
    X/=4
    print(f"{X:.4f}")
elif U1 == "SOK" and U2 == "SEN":
    X/=4
    X/=20
    print(f"{X:.4f}")
elif U1 == "WA" and U2 == "NIU":
    X*=12
    X*=2
    X*=4
    print(f"{X:.4f}")
elif U1 == "WA" and U2 == "KUEP":
    X*=2
    X*=4
    print(f"{X:.4f}")
elif U1 == "WA" and U2 == "SOK":
    X*=4
    print(f"{X:.4f}")
elif U1 == "WA" and U2 == "SEN":
    X/=20
    print(f"{X:.4f}")
elif U1 == "SEN" and U2 == "NIU":
    X*=12
    X*=2
    X*=4
    X*=20
    print(f"{X:.4f}")
elif U1 == "SEN" and U2 == "KUEP":
    X*=2
    X*=4
    X*=20
    print(f"{X:.4f}")
elif U1 == "SEN" and U2 == "SOK":
    X*=4
    X*=20
    print(f"{X:.4f}")
elif U1 == "SEN" and U2 == "WA":
    X*=20
    print(f"{X:.4f}")
