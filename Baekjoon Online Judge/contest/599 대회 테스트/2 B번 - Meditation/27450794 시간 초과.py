import sys

N, K = map(int, sys.stdin.readline().split())

status_now = [0]*(K+1)
status_next = [0]*(K+1)

for g in map(int, sys.stdin.readlines()):
    for k in range(1, K+1):
        status_next[k] = max(status_now[k], status_now[k-1]+g)
    status_now, status_next = status_next, status_now

print(max(status_now))
