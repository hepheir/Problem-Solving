MOD = 10007

TILE_1X2 = 0
TILE_2X1_L = 1
TILE_2X1_R = 2
TILE_2X2_L = 3
TILE_2X2_R = 4

N = int(input())

dp_old = [0, 0, 0, 0, 0]
dp_now = [0, 0, 0, 0, 0]

# N=1
dp_now[TILE_1X2] = 1
dp_now[TILE_2X1_L] = 1
dp_now[TILE_2X2_L] = 1

for n in range(2, N+1):
    dp_old, dp_now = dp_now, dp_old
    dp_all = sum([dp_old[tile] for tile in [TILE_1X2, TILE_2X1_R, TILE_2X2_R]]) % MOD
    dp_now[TILE_1X2]   = dp_all
    dp_now[TILE_2X1_L] = dp_all
    dp_now[TILE_2X2_L] = dp_all
    dp_now[TILE_2X1_R] = dp_old[TILE_2X1_L]
    dp_now[TILE_2X2_R] = dp_old[TILE_2X1_L]

ans = sum([dp_now[tile] for tile in [TILE_1X2, TILE_2X1_R, TILE_2X2_R]]) % MOD
print(ans)