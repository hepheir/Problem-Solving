import sys

N, M = map(int, sys.stdin.readline().split())

# Floyd-Warchall
FW = [[6] * (N+1) for n in range(N+1)]

def set_bacon_level(a, b, level):
    FW[a][b] = level
    FW[b][a] = level

for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    set_bacon_level(A, B, 1)
for n in range(N+1):
    set_bacon_level(n, 0, 0)
    set_bacon_level(n, n, 0)

for r in range(1,N+1): # 경유지 노드 (route)
    for a in range(1,N+1):
        for b in range(1,N+1):
            if a == b: continue
            bacon_level = FW[a][r]+FW[r][b]
            set_bacon_level(a, b, min(bacon_level, FW[a][b]))

min_bacon_level = 6*N
answer = None
for n in range(1, N+1):
    bacon_level = sum(FW[n])
    if bacon_level < min_bacon_level:
        min_bacon_level = bacon_level
        answer = n
        if min_bacon_level < N: break

print(answer)