from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, maxsize
from typing import DefaultDict, Dict, List, Tuple


_T_distance = int
_T_node = int


def dijkstra(graph: Dict[int, Dict[int, int]],
             root: int) -> Tuple[DefaultDict[int, int], Dict[int, int]]:
    heap: List[Tuple[_T_distance, _T_node]] = []

    distance = defaultdict(lambda: maxsize)
    parent = dict()

    distance[root] = 0
    heappush(heap, (distance[root], root))

    while heap:
        dist, node = heappop(heap)

        if dist > distance[node]:
            continue

        for child, weight in graph[node].items():
            new_dist = dist + weight

            if new_dist <= distance[child]:
                distance[child] = new_dist
                parent[child] = node
                heappush(heap, (new_dist, child))

    return distance, parent


def solution():
    graph: DefaultDict[int, Dict[int, int]] = defaultdict(lambda: dict())
    # graph[u][v] = w (u노드에서 v노드로 갈때의 가중치 w)

    n = int(stdin.readline())
    m = int(stdin.readline())

    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        graph[u][v] = w

    s, e = map(int, stdin.readline().split())

    distance, parent = dijkstra(graph, s)

    path = [e]
    node = e
    while node != s:
        node = parent[node]
        path.append(node)
    path.reverse()

    print(distance[e])
    print(len(path))
    print(' '.join(map(str, path)))


if __name__ == '__main__':
    solution()
