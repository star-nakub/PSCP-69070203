"""สมดุลย์ชีวิต"""
N = int(input())
hours = []
for _ in range(N):
    hours.append(int(input()))
heavy = sum(h > 18 for h in hours)
light = N - heavy
rest_days = max(0, heavy - 1 - light)
print(N + rest_days)
