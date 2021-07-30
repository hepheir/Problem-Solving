import collections
import sys


def solve():
    N, M = map(int, sys.stdin.readline().split())

    dst = [_ for _ in range(101)]
    for _ in range(N+M):
        x, y = map(int, sys.stdin.readline().split())
        dst[x] = y

    deque = collections.deque([1])
    dices = 0
    while True:
        for w in range(len(deque)):
            x = deque.popleft()

            if x == 100:
                return dices

            if dst[x] != x:
                x = dst[x]

            for d in range(1, 7):
                deque.append(x+d)

        dices += 1

print(solve())