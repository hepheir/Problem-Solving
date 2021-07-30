import heapq
import sys

minHeap = []
maxHeap = []

for t in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())
    # 해당 테스트 케이스를 위해 초기화
    isValid = [True] * K
    minHeap.clear()
    maxHeap.clear()
    for k in range(K):
        line = sys.stdin.readline().rstrip()
        # 최대값 제거
        if line == 'D 1':
            # 유효하지 않은 값 제거
            while maxHeap and (not isValid[maxHeap[0][1]]): heapq.heappop(maxHeap)
            # 힙이 비었다면 무시
            if not maxHeap: continue
            isValid[heapq.heappop(maxHeap)[1]] = False
        # 최소값 제거
        elif line == 'D -1':
            # 유효하지 않은 값 제거
            while minHeap and (not isValid[minHeap[0][1]]): heapq.heappop(minHeap)
            # 힙이 비었다면 무시
            if not minHeap: continue
            isValid[heapq.heappop(minHeap)[1]] = False
        # 값 삽입
        else:
            num = int(line.split()[1])
            heapq.heappush(minHeap, (num, k))
            heapq.heappush(maxHeap, (-num, k)) # 값의 부호를 뒤집어 최소힙을 최대힙처럼 사용
    # 유효하지 않은 값 제거
    while minHeap and (not isValid[minHeap[0][1]]): heapq.heappop(minHeap)
    while maxHeap and (not isValid[maxHeap[0][1]]): heapq.heappop(maxHeap)
    # 남아있는 최대, 최소값 출력
    if minHeap and maxHeap:
        minNum, k = heapq.heappop(minHeap)
        maxNum, k = heapq.heappop(maxHeap)
        print(-maxNum, minNum)
    else:
        print('EMPTY')
