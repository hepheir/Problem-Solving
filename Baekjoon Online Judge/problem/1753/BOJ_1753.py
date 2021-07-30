from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin
from typing import DefaultDict, Dict, Union


def dijkstra(graph: Dict[int, Dict[int, int]], root: int) -> DefaultDict[int, Union[int, float]]:
    heap = []
    distances = defaultdict(lambda: float('inf'))
    distances[root] = 0
    heappush(heap, (distances[root], root))

    while heap:
        dist, node = heappop(heap)

        if dist > distances[node]:
            continue

        for child, weight in graph[node].items():
            new_dist = dist + weight

            if new_dist > distances[child]:
                continue

            distances[child] = new_dist
            heappush(heap, (new_dist, child))

    return distances


def solution():
    V, E = map(int, stdin.readline().split())
    K = int(stdin.readline())

    graph = defaultdict(lambda: dict())

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())

        if v not in graph[u] or w < graph[u][v]:
            graph[u][v] = w

    distances = dijkstra(graph, K)

    for u in range(1, V+1):
        print(str(distances[u]).upper())


if __name__ == '__main__':
    # import io
    # stdin = io.TextIOWrapper(io.BytesIO())
    # stdin.write('5 6\n'
    #             '1\n'
    #             '5 1 1\n'
    #             '1 2 2\n'
    #             '1 3 3\n'
    #             '2 3 4\n'
    #             '2 4 5\n'
    #             '3 4 6\n')
    # stdin.seek(0)
    solution()
