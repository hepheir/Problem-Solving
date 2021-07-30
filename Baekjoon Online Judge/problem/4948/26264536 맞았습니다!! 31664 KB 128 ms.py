import sys

MAX_N = 123456*2

eratos = [True] * (MAX_N+1)
eratos[0], eratos[1] = False, False
for i in range(2, int(MAX_N**0.5)+1):
    if eratos[i]:
        for j in range(2*i, MAX_N+1, i):
            eratos[j] = False

primes = [num for num, is_prime in enumerate(eratos) if is_prime]

def bin_search(x):
    start = 0
    end = len(primes)-1
    while start <= end:
        mid = (start+end)//2
        if primes[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return start

for n in map(int, sys.stdin.readlines()[:-1]):
    print(bin_search(2*n) - bin_search(n))
