from collections import defaultdict

m, n = map(int, input().split())

# Sieve of Eratosthenes
sieve = defaultdict(lambda: True)
for i in range(2, int(n**0.5)+2):
    if sieve[i]:
        for j in range(2*i, n+1, i):
            sieve[j] = False

for i in range(m, n+1):
    if sieve[i]:
        print(i)