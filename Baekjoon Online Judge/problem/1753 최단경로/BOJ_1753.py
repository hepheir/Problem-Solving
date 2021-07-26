from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from sys import stdin
from typing import Deque, List


@dataclass
class Edge:
    start: Node # 출발할 노드
    end: Node # 도착할 노드
    weight: int # 가중치


@dataclass
class Node:
    cost: int | None = field(default=None) # dp로 구할 0부터 이 노드까지의 최단 경로(누적 가중치)
    edges: List[Edge] = field(default_factory=lambda: list())


def solution():
    V, E = map(int, stdin.readline().split())
    K = int(stdin.readline())

    graph = [Node() for _ in range(V+1)]
    root = graph[K]

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        edge = Edge(start=graph[u],
                    end=graph[v],
                    weight=w)
        graph[u].edges.append(edge)

    root.cost = 0
    queue: Deque[Node] = deque([root])
    while queue:
        node = queue.popleft()
        for edge in node.edges:
            new_cost = edge.start.cost + edge.weight
            if (edge.end.cost is None) or (new_cost < edge.end.cost):
                edge.end.cost = new_cost
                queue.append(edge.end)

    for node in graph[1:]:
        if node.cost is None:
            print('INF')
        else:
            print(node.cost)


if __name__ == '__main__':
    solution()
