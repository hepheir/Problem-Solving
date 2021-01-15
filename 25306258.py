import sys
sys.setrecursionlimit(10**6)

def dfs(root):
    subtree_size[root] = 1
    for node in graph[root]:
        if not subtree_size[node]: # not visited
            dfs(node)
            subtree_size[root] += subtree_size[node]

N, R, Q = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
subtree_size = [0] * (N+1)

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)

for u in map(int, sys.stdin.readlines()):
    print(subtree_size[u])