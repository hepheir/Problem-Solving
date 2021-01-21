import sys

points = []

N = int(sys.stdin.readline())
for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x,y))

points.sort()

for p in points:
    print(' '.join(map(str, p)))