"""port"""
N,K = map(int,input().split())
L1 = []
for x in range(K):
    L1.append(int(x+1))
L2 = []
for _ in range(N):
    if not _ :
        pass
    a = input()
    L2.append(int(a))
cont = [L2.count(n) for n in L1]
total = sum(cont)
left = total - K * min(cont)
print(left)
