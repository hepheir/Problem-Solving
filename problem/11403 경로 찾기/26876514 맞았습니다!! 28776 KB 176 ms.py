import sys

N = int(sys.stdin.readline())
distance = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

# Floyd-Warshall Algorithm

for r in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][j]: continue
            if dist := distance[i][r]*distance[r][j]:
                distance[i][j] = dist

def cell(x:int) -> str:
    return '1' if x > 0 else '0'

sys.stdout.write('\n'.join([' '.join(map(cell, distance[i])) for i in range(N)]))
