import sys
sys.setrecursionlimit(10**6)

def count_subtree_size(root):
    subtree_size[root] = 1
    for node in connect[root]:
        if not subtree_size[node]:
            count_subtree_size(node)
            subtree_size[root] += subtree_size[node]

N, R, Q = map(int, sys.stdin.readline().split())

connect = [[] for n in range(N+1)]
subtree_size = [0] * (N+1)

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    connect[u].append(v)
    connect[v].append(u)

count_subtree_size(R)

for u in (map(int, sys.stdin.readlines())):
    print(subtree_size[u])