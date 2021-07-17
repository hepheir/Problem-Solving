import collections
import sys

MATURE = 1
IMMATURE = 0
EMPTY = -1

X, Y, Z = map(int, sys.stdin.readline().split())
deque = collections.deque()
immatures = 0
days = 0

# Make Box
BOX = []
for z in range(Z):
    BOX.append([])  # Append a face
    for y in range(Y):
        BOX[z].append([])  # Append a row
        for x, status in enumerate(map(int, sys.stdin.readline().split())):
            BOX[z][y].append(status)
            if status == MATURE:
                deque.append((z, y, x, days))
            elif status == IMMATURE:
                immatures += 1


while deque and immatures:
    z, y, x, days = deque.popleft()
    days += 1
    if x > 0 and BOX[z][y][x-1] == IMMATURE:
        BOX[z][y][x-1] = MATURE
        immatures -= 1
        deque.append((z, y, x-1, days))

    if x < X-1 and BOX[z][y][x+1] == IMMATURE:
        BOX[z][y][x+1] = MATURE
        immatures -= 1
        deque.append((z, y, x+1, days))

    if y > 0 and BOX[z][y-1][x] == IMMATURE:
        BOX[z][y-1][x] = MATURE
        immatures -= 1
        deque.append((z, y-1, x, days))

    if y < Y-1 and BOX[z][y+1][x] == IMMATURE:
        BOX[z][y+1][x] = MATURE
        immatures -= 1
        deque.append((z, y+1, x, days))

    if z > 0 and BOX[z-1][y][x] == IMMATURE:
        BOX[z-1][y][x] = MATURE
        immatures -= 1
        deque.append((z-1, y, x, days))

    if z < Z-1 and BOX[z+1][y][x] == IMMATURE:
        BOX[z+1][y][x] = MATURE
        immatures -= 1
        deque.append((z+1, y, x, days))

print('-1' if immatures else days)
