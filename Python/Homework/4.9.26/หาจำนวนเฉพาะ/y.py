"""หาจำนวนเฉพาะ"""
start, end = map(int, input().split())
primes = []
for n in range(start, end + 1):
    if n < 2:
        continue
    prime = True
    for i in range(2, n):
        if not n % i:
            prime = False
            break
    if prime:
        primes.append(n)
print(*primes)
print("Total primes:", len(primes))
