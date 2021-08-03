from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, maxsize
from typing import DefaultDict, Dict, List, Tuple


def dijkstra(graph: Dict[int, Dict[int, int]],
             root: int) -> Tuple[DefaultDict[int, int], Dict[int, int]]:
    heap: List[Tuple[int, int, int]] = []

    distance = defaultdict(lambda: maxsize)
    parent = dict()

    root_node = root
    root_dist = 0
    root_waypoints = 0
    heappush(heap, (root_dist, root_waypoints, root_node))

    while heap:
        dist, waypoints, node = heappop(heap)

        if dist > distance[node]:
            continue

        for child, weight in graph[node].items():
            new_dist = dist + weight

            if new_dist <= distance[child]:
                distance[child] = new_dist
                parent[child] = node
                heappush(heap, (new_dist, waypoints+1, child))

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
