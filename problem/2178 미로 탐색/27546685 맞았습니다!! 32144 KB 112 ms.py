import collections
import sys

WALL = '0'
INF = sys.maxsize

N, M = map(int, sys.stdin.readline().split())
MIRO = [list(sys.stdin.readline().rstrip()) for n in range(N)]

moves = 1
dp = [[INF]* M for n in range(N)]
deque = collections.deque([(0,0, moves)])

while deque:
    y, x, moves = deque.popleft()

    if x < 0 or M <= x: continue
    if y < 0 or N <= y: continue
    if MIRO[y][x] == WALL: continue

    if dp[y][x] > moves:
        dp[y][x] = moves

        moves += 1
        deque.append((y, x+1, moves))
        deque.append((y, x-1, moves))
        deque.append((y+1, x, moves))
        deque.append((y-1, x, moves))

print(dp[N-1][M-1])
