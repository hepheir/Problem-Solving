from __future__ import annotations

import dataclasses
import heapq
import sys
import typing


@dataclasses.dataclass()
class Node:
    value: int

    def __lt__(self, node:Node):
        return self.value > node.value


heap:typing.List[Node] = []

for n in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x > 0:
        node = Node(x)
        heapq.heappush(heap, node)
    elif not heap:
        print('0')
    else:
        node = heapq.heappop(heap)
        print(node.value)
    