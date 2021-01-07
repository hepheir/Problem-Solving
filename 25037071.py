import collections
import sys
sys.setrecursionlimit(10**9)

graph = collections.defaultdict(list)
dfs_visited = collections.defaultdict(lambda: False)
bfs_visited = collections.defaultdict(lambda: False)
dfs_log = []
bfs_log = []

def dfs(node):
    dfs_log.append(str(node))
    dfs_visited[node] = True
    for n in graph[node]:
        if not dfs_visited[n]:
            dfs(n)

def bfs(node):
    stack = [node]
    while stack:
        n = stack.pop(0)
        if not bfs_visited[n]:
            bfs_log.append(str(n))
            bfs_visited[n] = True
            stack += graph[n]

N, M, V = map(int, sys.stdin.readline().split())
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for n in range(1, N+1):
    graph[n].sort()

dfs(V)
bfs(V)

print(' '.join(dfs_log))
print(' '.join(bfs_log))