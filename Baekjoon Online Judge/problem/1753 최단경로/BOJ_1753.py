from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from sys import stdin
from typing import Deque, Dict


@dataclass
class Node:
    cost: int | None = field(default=None) # dp로 구할 0부터 이 노드까지의 최단 경로(누적 가중치)
    edges: Dict[Node, int] = field(default_factory=lambda: dict()) # 간선 정보가 담긴 딕셔너리 {도착노드: 가중치}


def solution():
    V, E = map(int, stdin.readline().split())
    K = int(stdin.readline())

    nodes = [Node() for _ in range(20000+1)]

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())

        # 동일한 노드로 향하는 간선이 여러 개 있다면, 최단경로만 남김
        if v in nodes[u].edges:
            nodes[u].edges[v] = min(w, nodes[u].edges[v])
        else:
            nodes[u].edges[v] = w

    nodes[K].cost = 0
    queue: Deque[Node] = deque([K])
    while queue:
        u = queue.popleft()
        for v in nodes[u].edges:
            new_cost = nodes[u].cost + nodes[u].edges[v]
            if (nodes[v].cost is None) or (new_cost < nodes[v].cost):
                nodes[v].cost = new_cost
                queue.append(v)

    for u in range(1, V+1):
        if nodes[u].cost is None:
            print('INF')
        else:
            print(nodes[u].cost)


if __name__ == '__main__':
    solution()
