import sys

N, M = map(int, sys.stdin.readline().split())

deafen = set([sys.stdin.readline().rstrip() for n in range(N)])
blinds = set([sys.stdin.readline().rstrip() for m in range(M)])

answer = deafen & blinds
print(len(answer))
for name in sorted(answer):
    print(name)
