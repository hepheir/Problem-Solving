import sys

MAX_N = 10000

eratos = [True] * (MAX_N+1)
eratos[0], eratos[1] = False, False
for i in range(2, MAX_N+1):
    if eratos[i]:
        for j in range(2*i, MAX_N+1, i):
            eratos[j] = False
    
for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    for a in range(n//2, 0, -1):
        b = n-a
        if eratos[a] and eratos[b]:
            print(a, b)
            break