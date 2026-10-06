"""กระต่ายน้อยรัก BUU"""
txt = input().strip()
upper = txt.upper()
if "BUU" in upper:
    most = 0
    for i, ch in enumerate(upper):
        if ch == "B" and upper[i + 1:i + 3] == "UU":
            run = 0
            for c in upper[i + 1:]:
                if c == "U":
                    run += 1
                else:
                    break
            most = max(most, run)
    print("Yes", most)
elif "B" in upper:
    dd = upper.index("B")
    print(txt[:dd + 1] + "U" * (len(txt) - dd - 1))
else:
    pattern = ("BUU" * (len(txt) // 3 + 1))[:len(txt)]
    print(pattern)
