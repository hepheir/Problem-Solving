import sys

N = int(sys.stdin.readline())
lines = [tuple(map(int, sys.stdin.readline().split())) for n in range(N)]

lines.sort()

length = 0
pivot = -int(1e9+1)

for x, y in lines:
    length += (y-x) if (pivot < x) else (y-pivot)
    pivot = y

print(length)