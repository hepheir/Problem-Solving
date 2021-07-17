import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
parent = [None] * (N+1)
dp = [1] * (N+1)

maxlen = 0
seqend = 0
for n in range(N):
    for m in range(n):
        if not A[m] < A[n]:
            continue
        if dp[m] >= dp[n]:
            dp[n] = dp[m]+1
            parent[n] = m
            if dp[n] > maxlen:
                maxlen = dp[n]
                seqend = n

sequence = []
while seqend is not None:
    sequence.append(A[seqend])
    seqend = parent[seqend]
print(len(sequence))
print(' '.join(map(str, reversed(sequence))))