import sys


def make(m, n):
    visited = dict()
    x, y = 1, 1
    while True:
        if (x,y) in visited: break
        visited[x,y] = True
        yield x, y
        x = x+1 if (x < m) else 1
        y = y+1 if (y < n) else 1

def solve(m, n, x, y):
    for idx, (tx, ty) in enumerate(make(m, n)):
        if tx == x and ty == y:
            print(idx+1)
            return
    print('-1')

for t in range(int(sys.stdin.readline())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    solve(M, N, x, y)
    