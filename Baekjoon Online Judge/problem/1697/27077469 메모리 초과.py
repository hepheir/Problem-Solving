import collections

N, K = map(int, input().split())

deque = collections.deque([(N, 0)])

while deque:
    value, seconds = deque.popleft()
    if value == K:
        print(seconds)
        break
    else:
        deque.append((value*2, seconds+1))
        deque.append((value+1, seconds+1))
        deque.append((value-1, seconds+1))
