import itertools
import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0]*(K+1) for n in range(N)]

dp[0][1] = int(sys.stdin.readline())
i = 1

for g in map(int, sys.stdin.readlines()):
    for k in range(1, K+1):
        dp[i][k] = max(dp[i-1][k], dp[i-1][k-1]+g)
    i += 1

print(max(dp[-1]))
