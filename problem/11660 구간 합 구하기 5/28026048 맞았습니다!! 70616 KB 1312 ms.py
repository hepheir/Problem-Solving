import sys

sys.setrecursionlimit(10**6)


def solve():
    N, M = map(int, sys.stdin.readline().split())

    # (0, 0) 부터 (x, y)까지의 합을 미리 구해놓음
    DP = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

    for x in range(N):
        for y in range(N):
            if (x > 0):
                DP[x][y] += DP[x-1][y]
            if (y > 0):
                DP[x][y] += DP[x][y-1]
            if (x > 0) and (y > 0):
                DP[x][y] -= DP[x-1][y-1]

    # (sx, sy) 부터 (ex, ey) 까지 구하는 함수
    def query(sx, sy, ex, ey):
        if (sx > ex) or (sy > ey):
            return 0
        if (sx == 0) and (sy == 0):
            return DP[ex][ey]
        return query(0, 0, sx-1, sy-1) - query(0, 0, sx-1, ey) - query(0, 0, ex, sy-1) + query(0, 0, ex, ey)


    for m in range(M):
        x1, y1, x2, y2 = map(lambda x: int(x)-1, sys.stdin.readline().split())
        print(query(x1, y1, x2, y2))


solve()
