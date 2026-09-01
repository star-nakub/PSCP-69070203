"""ของขวัญและขโมย"""
N, K, T = map(int, input().split())
person = 1
count = 1
while True:
    if person == T:
        break
    person = (person + K - 1) % N + 1
    if person == 1:
        break
    count += 1
print(count)
