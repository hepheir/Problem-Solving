import dataclasses
import heapq
import sys

@dataclasses.dataclass(order=True)
class Node:
    priority:int
    value:int

N = int(sys.stdin.readline())

heap = []

for x in sys.stdin.readlines():
    x = x.rstrip()
    if x == '0' and heap:
        node = heapq.heappop(heap)
        print(node.value)
    elif x == '0' and not heap:
        print('0')
    else:
        heapq.heappush(heap, Node(abs(int(x)), x))
