from sys import stdin
from heapq import heappush, heappop

heap = []

N = int(stdin.readline())
for n in range(N):
    heappush(heap, int(stdin.readline()))
while heap:
    print(heappop(heap))