"""wow score"""
score = float(input())
max_score = float(input())
other_sum = score - max_score
min_score = max(0, other_sum - max_score)
if max_score - min_score > 2:
    print("Surprising")
else:
    print("Not surprising")
