import sys

N = int(sys.stdin.readline())
PAPER = []
ANSWER = {-1: 0, 0: 0, 1: 0}

for n in range(N):
    PAPER.append(list(map(int, sys.stdin.readline().split())))

def is_cutable(x, y, w, h):
    pivot = PAPER[y][x]
    for cx in range(x, x+w):
        for cy in range(y, y+h):
            if PAPER[cy][cx] != pivot:
                return True
    return False


def solve(x, y, w, h):
    if not is_cutable(x, y, w, h):
        ANSWER[PAPER[y][x]] += 1
        return
    for i in range(3):
        for j in range(3):
            solve(x + w*i//3, y + h*j//3, w//3, h//3)

solve(0, 0, N, N)
print(ANSWER[-1])
print(ANSWER[0])
print(ANSWER[1])