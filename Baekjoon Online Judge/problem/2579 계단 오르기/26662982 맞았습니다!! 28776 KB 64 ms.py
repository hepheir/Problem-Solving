import sys

STAIRS = int(sys.stdin.readline())
PHYSICAL = 2

dp = [[0]*PHYSICAL] + [[int(sys.stdin.readline())]*PHYSICAL for n in range(STAIRS)]

for i in range(2, STAIRS+1):
    dp[i][0] += max(dp[i-2])
    dp[i][1] += dp[i-1][0]

print(max(dp[STAIRS]))