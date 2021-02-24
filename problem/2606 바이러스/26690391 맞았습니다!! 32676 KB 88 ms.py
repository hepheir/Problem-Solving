import sys
import collections

COMPUTERS = int(sys.stdin.readline())
ON_NETWORK = int(sys.stdin.readline())

graph = [[] for n in range(COMPUTERS+1)]
for n in range(ON_NETWORK):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

queue = collections.deque([1])
visited = [False] * (COMPUTERS+1)
answer = 0
while queue:
    node = queue.popleft()
    if not visited[node]:
        visited[node] = True
        queue.extend(graph[node])
        answer += 1

print(answer-1)
