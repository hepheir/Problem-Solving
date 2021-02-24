import sys
import collections

COMPUTERS = int(sys.stdin.readline())
ON_NETWORK = int(sys.stdin.readline())

graph = collections.defaultdict(list)
for n in range(ON_NETWORK):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

queue = collections.deque([1])
visited = collections.defaultdict(lambda: False)
answer = 0
while queue:
    node = queue.popleft()
    if not visited[node]:
        visited[node] = True
        queue.extend(graph[node])
        answer += 1

print(answer-1)
