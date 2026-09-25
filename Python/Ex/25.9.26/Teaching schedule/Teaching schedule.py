"""Teaching schedule"""
N = int(input())
A = int(input())
TIME = N*A
HR = TIME // 60
MIN = TIME % 60
if not TIME:
    print("No teaching")
elif MIN > 0 and HR > 0:
    print(f"{HR} hours {MIN} minute")
elif not MIN:
    print(f"{HR} hours")
elif not HR:
    print(f"{MIN} minute")
