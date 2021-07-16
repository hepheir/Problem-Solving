import sys

N, K = map(int, sys.stdin.readline().split())

answer = 0
for g in sorted(map(int, sys.stdin.readlines()), reverse=True):
    answer += g
    if (K := K-1) == 0:
        break

print(answer)
