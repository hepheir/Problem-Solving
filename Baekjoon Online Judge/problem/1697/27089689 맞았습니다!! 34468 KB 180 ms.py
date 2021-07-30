import collections

MAX_N = 100000

N, K = map(int, input().split())

visited = [False] * (MAX_N+1)

deque = collections.deque([(N, 0)])
visited[N] = True
answer = 0
while deque:
    x, depth = deque.popleft()
    if x == K:
        answer = depth
        break
    for y in (x*2, x+1, x-1):
        if (0 <= y <= MAX_N) and (not visited[y]):
            visited[y] = True
            deque.append((y, depth+1))

print(answer)
