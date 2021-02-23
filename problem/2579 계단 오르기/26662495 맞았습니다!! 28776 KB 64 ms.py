import sys

# 계단 최대 개수
MAX_N = 300

# 지금 계단 수
N = int(sys.stdin.readline())

# 0으로 초기화 된 Nx3 크기 배열 선언
# dp[a][b]: b는 a번째 계단 이전까지 연속해서 밟은 계단의 수
#
# 0: 지금까지 연속해서 밟지 않음 (본인 제외)
# 1: 지금까지 1개 연속해서 밟음 (본인 제외)
dp = [ [0] * 2 ]
for n in range(N):
    dp.append([int(sys.stdin.readline())] * 2)

for i in range(2, N+1):
    dp[i][0] += max(dp[i-2])
    dp[i][1] += dp[i-1][0]

print(max(dp[N]))