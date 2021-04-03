import sys


def solve():
    N = int(sys.stdin.readline())

    dp_r, dp_g, dp_b = 0, 0, 0

    for n in range(N):
        last_r, last_g, last_b = dp_r, dp_g, dp_b
        cost_r, cost_g, cost_b = map(int, sys.stdin.readline().split())
        dp_r = cost_r + min(last_g, last_b)
        dp_g = cost_g + min(last_r, last_b)
        dp_b = cost_b + min(last_r, last_g)

    return min(dp_r, dp_g, dp_b)


print(solve())