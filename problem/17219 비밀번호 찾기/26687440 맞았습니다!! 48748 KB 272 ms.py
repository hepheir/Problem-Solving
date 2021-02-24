import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

cached_password = dict()

for n in range(N):
    domain, password = sys.stdin.readline().rstrip().split()
    cached_password[domain] = password

for m in range(M):
    site = sys.stdin.readline().rstrip()
    print(cached_password[site])