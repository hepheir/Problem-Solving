import sys
import collections
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
answer = 0

def dfs(root):
    if not visited[root]:
        visited[root] = True
        for child in graph[root]:
            dfs(child)

for n in range(1,N+1):
    if not visited[n]:
        dfs(n)
        answer += 1

print(answer)