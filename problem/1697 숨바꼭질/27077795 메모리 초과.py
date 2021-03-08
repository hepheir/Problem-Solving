import collections

def solve(n, k):
    current_deque = collections.deque([n])
    future_dequq = collections.deque()
    for seconds in range(100000):
        for i in range(len(current_deque)):
            x = current_deque.popleft()
            if x == k:
                return seconds
            future_dequq.append(x<<1)
            future_dequq.append(x+1)
            future_dequq.append(x-1)
        current_deque, future_dequq = future_dequq, current_deque
    raise Exception('틀렸습니다')

N, K = map(int, input().split())

print(solve(N, K))