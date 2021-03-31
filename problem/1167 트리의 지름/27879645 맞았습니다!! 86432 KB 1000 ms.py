import collections
import sys


V = int(sys.stdin.readline())
graph = collections.defaultdict(set)

for _ in range(V):
    args = list(map(int, sys.stdin.readline().split()))
    v = args[0]
    for i in range(1, len(args)-1, 2):
        u = args[i]
        w = args[i+1]
        graph[v].add((u, w))
        graph[u].add((v, w))


far_node = 0
far_dist = 0

def dfs(x, visited, weights=0):
    global far_node, far_dist
    visited[x] = True
    if weights > far_dist:
        far_node = x
        far_dist = weights
    for nx, w in graph[x]:
        if not visited[nx]:
            dfs(nx, visited, weights+w)

visited = [False] * (V+1)
dfs(1, visited)

visited = [False] * (V+1)
dfs(far_node, visited)

print(far_dist)