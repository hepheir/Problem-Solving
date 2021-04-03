import sys


def solve():
    N, M = map(int, sys.stdin.readline().split())
    TABLE = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

    for m in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        answer = 0
        for x in range(x1-1, x2):
            for y in range(y1-1, y2):
                answer += TABLE[x][y]
        print(answer)


solve()
