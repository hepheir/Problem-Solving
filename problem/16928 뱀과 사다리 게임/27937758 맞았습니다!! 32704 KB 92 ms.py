import collections
import sys


def solve():
    N, M = map(int, sys.stdin.readline().split())

    dp = [sys.maxsize] * (101)
    dst = [_ for _ in range(101)]
    for _ in range(N+M):
        x, y = map(int, sys.stdin.readline().split())
        dst[x] = y

    deque = collections.deque([(1,0)])
    while True:
        x, dices = deque.popleft()

        # If meet a snake or a ladder
        if dst[x] != x:
            x = dst[x]

        if dp[x] > dices:
            dp[x] = dices
            for d in range(1, 7):
                deque.append((x+d, dices+1))

        if x == 100:
            break

    return dp[100]


print(solve())