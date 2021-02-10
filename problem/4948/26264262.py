import sys

MAX_N = 123456*2

eratos = [True] * (MAX_N+1)
eratos[0], eratos[1] = False, False
for i in range(2, int(MAX_N**0.5)+1):
    if eratos[i]:
        for j in range(2*i, MAX_N+1, i):
            eratos[j] = False

count = [0] * (MAX_N+1)
for i in range(1, MAX_N+1):
    count[i] = count[i-1]
    if eratos[i]:
        count[i] += 1

for n in map(int, sys.stdin.readlines()[:-1]):
    print(count[2*n]-count[n])
