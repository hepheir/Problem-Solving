import sys


def solve():
    N, M = map(int, sys.stdin.readline().split())
    PAPER = [[*map(int, sys.stdin.readline().split())] for n in range(N)]

    def dfs(x, y, count, px=-1, py=-1):
        # px, py 는 이전 좌표 (왔던 길 중복 방지용)
        # previous x
        # previous y
        # 이 함수로 'ㅗ' 패턴을 제외한 나머지 3 패턴 처리 가능
        if count <= 0:
            return 0
        if not ((0 <= x < M) and (0 <= y < N)):
            return 0
        maxsum = 0
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (nx == px) and (ny == py):
                continue
            maxsum = max(dfs(nx, ny, count-1, x, y), maxsum)
        return maxsum + PAPER[y][x]

    def exceptional_pattern(x, y):
        # 'ㅗ' 모양 처리를 위한 특수 함수
        bounds = []
        if (0 < x):
            bounds.append(PAPER[y][x-1])
        if (x < M-1):
            bounds.append(PAPER[y][x+1])
        if (0 < y):
            bounds.append(PAPER[y-1][x])
        if (y < N-1):
            bounds.append(PAPER[y+1][x])
        if len(bounds) == 4:
            return PAPER[y][x] + sum(bounds) - min(bounds)
        if len(bounds) == 3:
            return PAPER[y][x] + sum(bounds)
        return -sys.maxsize

    answer = 0
    for y in range(N):
        for x in range(M):
            answer = max(dfs(x, y, 4), answer)
            answer = max(exceptional_pattern(x, y), answer)
    return answer


print(solve())
