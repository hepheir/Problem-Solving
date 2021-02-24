import sys

MAX_N = 11
dp = [1] * (MAX_N+1)

for n in range(1, MAX_N+1):
    dp[n] = dp[n-1]
    if n >= 2:
        dp[n] += dp[n-2]
    if n >= 3:
        dp[n] += dp[n-3]

answers = []
for t in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    answers.append(str(dp[n]))
print('\n'.join(answers))
