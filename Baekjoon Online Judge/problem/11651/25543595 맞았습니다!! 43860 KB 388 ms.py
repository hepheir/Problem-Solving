from sys import stdin

points = []

for n in range(int(stdin.readline())):
    points.append(tuple(map(int, stdin.readline().split())))

points.sort()
points.sort(key=lambda x:x[1])

for p in points:
    print(*p)