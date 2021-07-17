import collections
import sys


V = int(sys.stdin.readline())
graph = collections.defaultdict(list)
answer = 0


for _ in range(V):
    args = list(map(int, sys.stdin.readline().split()))
    v = args[0]
    for i in range(1, len(args)-1, 2):
        u = args[i]
        w = args[i+1]
        graph[v].append((u, w))
        graph[u].append((v, w))


def dfs(x, visited, weights=0):
    global answer
    answer = max(weights, answer)
    visited[x] = True
    for nx, w in graph[x]:
        if not visited[nx]:
            dfs(nx, visited, weights+w)

for v in range(1, V+1):
    visited = [False] * (V+1)
    dfs(v, visited)

print(answer)