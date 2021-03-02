import sys

N = int(sys.stdin.readline())
TABLE = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

graph = [[j for j, dist in enumerate(TABLE[i]) if dist] for i in range(N)]

def dfs(i, visited):
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j, visited)

output_lines = []

for i in range(N):
    visited = [False]*N
    dfs(i, visited)
    output_lines.append(' '.join(['1' if visited[j] else '0' for j in range(N)]))

sys.stdout.write('\n'.join(output_lines))
