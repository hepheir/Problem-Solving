import sys


sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
PAINT = [[*sys.stdin.readline().rstrip()] for n in range(N)]


def apply_color_blindness():
    for y in range(N):
        for x in range(N):
            if PAINT[y][x] == 'G':
                PAINT[y][x] = 'R'


def dfs(y, x, visited):
    if visited.get((y, x), False):
        return
    visited[y, x] = True
    if (0 < x) and (PAINT[y][x-1] == PAINT[y][x]):
        dfs(y, x-1, visited)
    if (x+1 < N) and (PAINT[y][x+1] == PAINT[y][x]):
        dfs(y, x+1, visited)
    if (0 < y) and (PAINT[y-1][x] == PAINT[y][x]):
        dfs(y-1, x, visited)
    if (y+1 < N) and (PAINT[y+1][x] == PAINT[y][x]):
        dfs(y+1, x, visited)


def count_areas():
    visited = dict()
    area = 0
    for y in range(N):
        for x in range(N):
            if not visited.get((y, x), False):
                dfs(y, x, visited)
                area += 1
    return area


areas = count_areas()
apply_color_blindness()
areas_cblind = count_areas()
print(areas, areas_cblind)
