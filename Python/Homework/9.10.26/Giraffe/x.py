N = int(input())
h = []
for _ in range(N):
    h.append(int(input()))
count = 0
for i in range(1, N - 1):
    if h[i] > h[i - 1] and h[i] > h[i + 1]:
        count += 1
print(count)
