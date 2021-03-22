import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readlines()))

A.sort()
A.reverse()

answer = 0

for a in A:
    if K // a:
        answer += K // a
        K %= a

print(answer)
