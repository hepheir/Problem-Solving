from collections import defaultdict
from dataclasses import dataclass
from heapq import heappop, heappush
from sys import stdin, maxsize
from typing import DefaultDict, Dict, List, Tuple


@dataclass(order=True)
class DijkstraNode:
    distance: int
    waypoints: int
    id: int


def dijkstra(graph: Dict[int, Dict[int, int]],
             parent: Dict[int, int],
             root: int) -> DefaultDict[int, int]:
    distance = defaultdict(lambda: maxsize)

    heap: List[DijkstraNode] = []
    root_node = DijkstraNode(distance=0,
                             waypoints=0,
                             id=root)

    heappush(heap, root_node)

    while heap:
        node = heappop(heap)

        if node.distance > distance[node.id]:
            continue

        for child_id, weight in graph[node.id].items():
            child_node = DijkstraNode(
                id=child_id,
                distance=node.distance+weight,
                waypoints=node.waypoints+1)

            if child_node.distance < distance[child_id]:
                distance[child_id] = child_node.distance
                parent[child_id] = node.id
                heappush(heap, child_node)

    return distance


def solution():
    n = int(stdin.readline())
    m = int(stdin.readline())

    # graph[u][v] = w (u노드에서 v노드로 갈때의 가중치 w)
    graph: DefaultDict[int, Dict[int, int]] = defaultdict(lambda: dict())
    parent: DefaultDict[int, int] = defaultdict(lambda: -1)

    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        parent[v] = u
        graph[u][v] = w

    s, e = map(int, stdin.readline().split())

    if s == e:
        print(0)
        print(1)
        print(s)
        return

    else:
        distance = dijkstra(graph, parent, s)

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
