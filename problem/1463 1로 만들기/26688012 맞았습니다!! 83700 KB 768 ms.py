import sys

N = int(sys.stdin.readline())

dp = [sys.maxsize]*(3*N)

dp[N] = 0
for n in range(N-1, 0, -1):
    dp[n] = min(
        1+dp[n*3],
        1+dp[n*2],
        1+dp[n+1],
        dp[n]
    )

print(dp[1])
