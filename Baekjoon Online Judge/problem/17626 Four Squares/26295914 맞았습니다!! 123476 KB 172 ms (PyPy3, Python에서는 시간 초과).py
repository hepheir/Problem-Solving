N = int(input())
squares = [i**2 for i in range(int(N**0.5)+2)]
dp = [4] * (N+1)

dp[0], dp[1] = 0, 1
for i in range(2, N+1):
    j = 0
    while squares[j] <= i:
        dp[i] = min(dp[i-squares[j]], dp[i])
        if not dp[i]: break # 더 줄일 수 없음
        j += 1
    dp[i] += 1

print(dp[N])