import sys
import heapq # 최소 힙 모듈 사용

N = int(sys.stdin.readline())
heap = []

for n in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if not heap:
            print('0')
        else:
            x = -heapq.heappop(heap)
            print(x)
