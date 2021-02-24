import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()

answer = 0
for n, pi in enumerate(P):
    answer += pi*(N-n)
print(answer)