import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [1] * (N+1)
for n in range(N):
    for m in range(n):
        if sequence[m] < sequence[n]:
            dp[n] = max(dp[m]+1, dp[n])
print(max(dp))