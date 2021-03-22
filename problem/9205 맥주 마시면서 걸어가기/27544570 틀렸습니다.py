import collections
import sys

MAX_DISTANCE = 20*50


def manhattan_distance(src_x, src_y, dst_x, dst_y):
    return (dst_x-src_x) + (dst_y-src_y)


def solve():
    N = int(sys.stdin.readline())
    HOME = 0
    FEST = N+1
    graph = collections.defaultdict(list)
    nodes = [tuple(map(int, sys.stdin.readline().split())) for n in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                continue
            if abs(manhattan_distance(*nodes[i], *nodes[j])) <= MAX_DISTANCE:
                graph[i].append(j)
                graph[j].append(i)

    deque = collections.deque([HOME])
    visited = [False]*(N+2)
    while deque:
        node = deque.popleft()
        if node == FEST:
            return 'happy'
        if not visited[node]:
            visited[node] = True
            deque.extend(graph[node])
    return 'sad'


for t in range(int(sys.stdin.readline())):
    print(solve())
