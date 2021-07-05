from collections import deque
import sys
sys.setrecursionlimit(10**9)

def dfs(node):
    dfs_log.append(node)
    dfs_visited[node] = True
    for n in graph[node]:
        if not dfs_visited[n]:
            dfs(n)

def bfs(node):
    queue = deque([node])
    while queue:
        n = queue.popleft()
        if not bfs_visited[n]:
            bfs_log.append(n)
            bfs_visited[n] = True
            queue.extend(graph[n])

if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    graph = [[] for n in range(N+1)]
    dfs_visited = [False] * (N+1)
    bfs_visited = [False] * (N+1)
    dfs_log = []
    bfs_log = []
    for m in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    for n in range(1, N+1):
        graph[n].sort()

    dfs(V)
    bfs(V)

    print(' '.join(map(str, dfs_log)))
    print(' '.join(map(str, bfs_log)))