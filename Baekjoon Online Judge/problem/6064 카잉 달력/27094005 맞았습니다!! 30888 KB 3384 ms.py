import math
import sys

def solve(m, n, x, y):
    diff = x-y
    loop = 0
    while (diff + loop*m) % n:
        loop += 1
        if loop > (n // math.gcd(n,m)):
            return -1
    return loop * m + x

for t in range(int(sys.stdin.readline())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    k = solve(M, N, x, y)
    print(k)
