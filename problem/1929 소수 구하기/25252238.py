from collections import defaultdict
from math import ceil, sqrt

m, n = map(int, input().split())

# Sieve of Eratosthenes
is_prime = defaultdict(lambda: True)
for i in range(2, ceil(sqrt(n))+1):
    if is_prime[i]:
        for j in range(2*i, n+1, i):
            is_prime[j] = False

for i in range(m, n+1):
    if is_prime[i]:
        print(i)