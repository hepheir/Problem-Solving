import sys

def make(m, n):
    # M과 N으로 만들 수 있는 카잉달력 모두 생성
    yield 1, 1
    x, y = 2, 2
    while (x, y) != (1, 1):
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
