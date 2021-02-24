MOD = 10007

TILE_1X2 = 0
TILE_2X1_L = 1
TILE_2X1_R = 2

N = int(input())

dp = [[0, 0, 0] for n in range(N+1)]
dp[1] = [1, 1, 0]

for n in range(2, N+1):
    dp[n][TILE_1X2] = dp[n-1][TILE_1X2] + dp[n-1][TILE_2X1_R]
    dp[n][TILE_2X1_L] = dp[n-1][TILE_1X2] + dp[n-1][TILE_2X1_R]
    dp[n][TILE_2X1_R] = dp[n-1][TILE_2X1_L]

ans = (dp[N][TILE_1X2] + dp[N][TILE_2X1_R]) % MOD
print(ans)