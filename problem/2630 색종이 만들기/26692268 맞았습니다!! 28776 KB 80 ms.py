import sys

N = int(sys.stdin.readline())
PAPER = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

class Answer:
    white = 0
    blue = 0

def is_cutable(x, y, w, h):
    if w <= 1 or h <= 1: return False
    last_cell = PAPER[y][x]
    for _x in range(x, x+w):
        for _y in range(y, y+h):
            if PAPER[_y][_x] != last_cell: return True
    return False

def subprob(x, y, w, h):
    if not is_cutable(x, y, w, h):
        if PAPER[y][x] == 0:
            Answer.white += 1
        else:
            Answer.blue += 1
        return
    subprob(x,      y,      w//2, h//2)
    subprob(x,      y+h//2, w//2, h//2)
    subprob(x+w//2, y,      w//2, h//2)
    subprob(x+w//2, y+h//2, w//2, h//2)

subprob(0, 0, N, N)
print(Answer.white)
print(Answer.blue)