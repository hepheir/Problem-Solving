import sys

N = int(sys.stdin.readline())
BIN_IMAGE = [sys.stdin.readline().rstrip() for n in range(N)]


def dfs(y, x, n):
    if n == 1:
        return BIN_IMAGE[y][x]
    n >>= 1
    result = [
        dfs(y,   x,   n),
        dfs(y,   x+n, n),
        dfs(y+n, x,   n),
        dfs(y+n, x+n, n),
    ]
    if result[0] == result[1] == result[2] == result[3]:
        return result[0]
    else:
        return '('+''.join(result)+')'


print(dfs(0, 0, N))
