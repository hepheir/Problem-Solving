import sys

N = int(sys.stdin.readline())

dp = [[0]*4]*2

for n in range(2, N+1):
    dp_n = [N] * 4
    if n % 3 == 0:
        dp_n[1] = 1 + min(dp[n//3])
    if n % 2 == 0:
        dp_n[2] = 1 + min(dp[n//2])
    dp_n[3] = 1 + min(dp[n-1])
    dp.append(dp_n)

print(min(dp[N]))
