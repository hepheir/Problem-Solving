import sys

N = int(sys.stdin.readline())

dp = [N]*(N+1)

dp[N] = 0
for n in range(N, 0, -1):
    if n % 3 == 0:
        dp[n//3] = min(1+dp[n], dp[n//3])
    if n % 2 == 0:
        dp[n//2] = min(1+dp[n], dp[n//2])
    dp[n-1] = min(1+dp[n], dp[n-1])

print(dp[1])
