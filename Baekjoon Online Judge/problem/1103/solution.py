import functools
import sys


MAX_N = 50

sys.setrecursionlimit(10*(MAX_N**2))

H, W = map(int, sys.stdin.readline().split())
BOARD = [[*map(int, sys.stdin.readline().strip().replace('H', '0'))] for _ in range(H)]


visited = [[False] * W for _ in range(H)]


@functools.cache
def backtracking(y: int, x: int) -> int:
    if not (0 <= y < H and 0 <= x < W) or BOARD[y][x] == 0:
        return 0
    if visited[y][x]:
        return -1
    max_val = 0
    visited[y][x] = True
    X = BOARD[y][x]
    for ny, nx in [(y-X, x), (y+X, x), (y, x-X), (y, x+X)]:
        val = backtracking(ny, nx)
        if val == -1:
            return -1
        if max_val < val+1:
            max_val = val+1
    visited[y][x] = False
    return max_val


print(backtracking(0, 0))
