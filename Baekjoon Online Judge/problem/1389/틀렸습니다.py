import sys
import collections

N, M = map(int, sys.stdin.readline().split())

graph = [[] for n in range(N+1)]

for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(root):
    visited = collections.defaultdict(lambda:False)
    bacon_number = 0
    def __bfs(node, depth):
        nonlocal bacon_number
        visited[node] = True
        bacon_number += depth
        for child in graph[node]:
            if not visited[child]:
                __bfs(child, depth+1)
    __bfs(root, 1)
    return bacon_number

min_bacon_number = N*6+1
answer = None
for n in range(1, N+1):
    bacon_number = bfs(n)
    if bacon_number < min_bacon_number:
        min_bacon_number = bacon_number
        answer = n
        if min_bacon_number == 1:
            break
print(answer)