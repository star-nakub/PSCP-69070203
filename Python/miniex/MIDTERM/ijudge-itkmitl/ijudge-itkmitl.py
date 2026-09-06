"""ijudge-itkmitl"""
IJUDGE = input()
PROB = IJUDGE.strip("https://ijudge.it.kmitl.ac.th/problems/")
M = IJUDGE.find("https://ijudge.it.kmitl.ac.th/problems/")
if not M:
    if len(PROB) == 4 or len(PROB) == 5:
        if PROB.endswith("/"):
            if PROB.startswith("0"):
                print("0 STAR")
            elif PROB.startswith("1"):
                print("1 STAR")
            elif PROB.startswith("2"):
                print("2 STAR")
            elif PROB.startswith("3"):
                print("3 STAR")
            else:
                print("INVALID")
        elif PROB.isdigit():
            if PROB.startswith("0"):
                print("0 STAR")
            elif PROB.startswith("1"):
                print("1 STAR")
            elif PROB.startswith("2"):
                print("2 STAR")
            elif PROB.startswith("3"):
                print("3 STAR")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")
