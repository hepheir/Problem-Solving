import sys

sys.setrecursionlimit(10**6)


def solve():
    N, M = map(int, sys.stdin.readline().split())
    PAPER = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

    answer = 0


    def dfs(x, y, length, sum=0, px=-1, py=-1, count=1):
        # px, py 는 이전 좌표 (왔던 길 중복 방지용)
        # previous x
        # previous y
        nonlocal answer
        if (count == length):
            answer = max(sum, answer)
        else:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx # next x
                ny = y + dy # next y
                if (nx == px) and (ny == py):
                    continue
                if (0 <= nx < M) and (0 <= ny < N):
                    dfs(nx, ny, length, sum+PAPER[ny][nx], x, y, count+1)


    def exceptional_pattern(x, y):
        # 'ㅗ' 모양 처리를 위한 특수 함수
        nonlocal answer
        if (0 <= x < M-1) and (1 <= y < N-1): # ㅏ
            answer = max(PAPER[y][x]+PAPER[y][x+1]+PAPER[y-1][x]+PAPER[y+1][x], answer)
        if (1 <= x < M-1) and (1 <= y < N): # ㅗ
            answer = max(PAPER[y][x]+PAPER[y][x-1]+PAPER[y][x+1]+PAPER[y-1][x], answer)
        if (1 <= x < M) and (1 <= y < N-1): # ㅓ
            answer = max(PAPER[y][x]+PAPER[y][x-1]+PAPER[y-1][x]+PAPER[y+1][x], answer)
        if (1 <= x < M-1) and (0 <= y < N-1): # ㅜ
            answer = max(PAPER[y][x]+PAPER[y][x-1]+PAPER[y][x+1]+PAPER[y+1][x], answer)

    for y in range(N):
        for x in range(M):
            dfs(x, y, 4, PAPER[y][x])
            exceptional_pattern(x, y)
    return answer


print(solve())
