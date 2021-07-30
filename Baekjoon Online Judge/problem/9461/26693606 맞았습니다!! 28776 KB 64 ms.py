import sys

P_cache = [None, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def P(n):
    if len(P_cache) <= n:
        for i in range(len(P_cache), n+1):
            Pi = P_cache[i-1] + P_cache[i-5]
            P_cache.append(Pi)
    return P_cache[n]

for t in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    print(P(N))
