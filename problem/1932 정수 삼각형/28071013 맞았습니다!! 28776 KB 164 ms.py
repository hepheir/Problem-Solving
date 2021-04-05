import sys


def solve():
    N = int(sys.stdin.readline())

    dp_prev = [0] * N
    dp_next = [0] * N

    for n in range(1, N+1):
        for idx, x in enumerate(map(int, sys.stdin.readline().split())):
            dp_next[idx] = x + max(dp_prev[max(idx-1, 0)], dp_prev[min(idx, n-1)])
        dp_next, dp_prev = dp_prev, dp_next

    return max(dp_prev)


print(solve())