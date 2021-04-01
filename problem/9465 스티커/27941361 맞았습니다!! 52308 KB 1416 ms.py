import sys


def solve():
    N = int(sys.stdin.readline())
    SCORE = list(zip(
        map(int, sys.stdin.readline().split()),
        map(int, sys.stdin.readline().split())
    ))

    dp = [[0, 0] for n in range(N)]

    dp[0][0] = SCORE[0][0]
    dp[0][1] = SCORE[0][1]

    if (N > 1):
        dp[1][0] = dp[0][1] + SCORE[1][0]
        dp[1][1] = dp[0][0] + SCORE[1][1]

        for n in range(2, N):
            dp[n][0] = max(dp[n-1][1], max(dp[n-2])) + SCORE[n][0]
            dp[n][1] = max(dp[n-1][0], max(dp[n-2])) + SCORE[n][1]

    return max(dp[-1])


T = int(sys.stdin.readline())
for t in range(T):
    print(solve())
