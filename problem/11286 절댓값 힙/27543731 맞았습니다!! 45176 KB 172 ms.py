import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for x in map(int, sys.stdin.readlines()):
    if x == 0:
        print(heapq.heappop(heap)[1] if heap else '0')
    else:
        heapq.heappush(heap, (abs(int(x)), x))
