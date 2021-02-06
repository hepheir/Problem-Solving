MAX_N = 10001

eratos = [True] * MAX_N
for i in range(int(MAX_N**0.5)+1):
    if i < 2:
        eratos[i] = False
    elif eratos[i]:
        for j in range(2*i, MAX_N, i):
            eratos[j] = False

m = int(input())
n = int(input())
primes = [i for i in range(m, n+1) if eratos[i]]
if primes:
    print(sum(primes))
    print(min(primes))
else:
    print('-1')