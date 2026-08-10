"""port"""
n, k = map(int, input().split())
queue = [0] * k
for i in range(n):
    x = int(input())
    queue[x - 1] += 1
print(n - sum(x > 0 for x in queue))