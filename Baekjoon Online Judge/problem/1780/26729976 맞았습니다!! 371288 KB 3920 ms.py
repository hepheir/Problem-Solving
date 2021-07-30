import sys

N = int(sys.stdin.readline())
PAPER = [sys.stdin.readline().split() for n in range(N)]
ANSWER = {'-1': 0, '0': 0, '1': 0}

def is_cutable(x, y, n):
    if n == 1: return False
    pivot = PAPER[y][x]
    for cx in range(x, x+n):
        for cy in range(y, y+n):
            if PAPER[cy][cx] != pivot:
                return True
    return False


def solve(x, y, n):
    if not is_cutable(x, y, n):
        ANSWER[PAPER[y][x]] += 1
        return
    for i in range(3):
        for j in range(3):
            solve(x+n*i//3, y+n*j//3, n//3)

solve(0, 0, N)
print(ANSWER['-1'])
print(ANSWER['0'])
print(ANSWER['1'])