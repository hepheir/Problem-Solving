import collections
import sys

MATURE = '1'
IMMATURE = '0'
EMPTY = '-1'

WIDTH, HEIGHT = map(int, sys.stdin.readline().split())
BOX = [sys.stdin.readline().split() for h in range(HEIGHT)]

today_deque = collections.deque()
tomorrow_deque = collections.deque()
immatures = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if BOX[y][x] == IMMATURE:
            immatures += 1
        elif BOX[y][x] == MATURE:
            today_deque.append((y,x))

days = 0
while today_deque and immatures:
    for _ in range(len(today_deque)):
        y, x = today_deque.popleft()
        if (x > 0) and (BOX[y][x-1] == IMMATURE):
            BOX[y][x-1] = MATURE
            tomorrow_deque.append((y, x-1))
            immatures -= 1
        if (y > 0) and (BOX[y-1][x] == IMMATURE):
            BOX[y-1][x] = MATURE
            tomorrow_deque.append((y-1, x))
            immatures -= 1
        if (x < WIDTH-1) and (BOX[y][x+1] == IMMATURE):
            BOX[y][x+1] = MATURE
            tomorrow_deque.append((y, x+1))
            immatures -= 1
        if (y < HEIGHT-1) and (BOX[y+1][x] == IMMATURE):
            BOX[y+1][x] = MATURE
            tomorrow_deque.append((y+1, x))
            immatures -= 1
    tomorrow_deque, today_deque = today_deque, tomorrow_deque
    days += 1

if immatures:
    print('-1')
else:
    print(days)