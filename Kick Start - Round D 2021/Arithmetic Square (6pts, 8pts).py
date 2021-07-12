from sys import stdin
from math import floor
from collections import Counter


def main():
    testcases = int(stdin.readline())

    for t in range(1, testcases+1):
        grid_3x3 = [
            list(map(int, stdin.readline().split())),
            list(map(int, stdin.readline().split())),
            list(map(int, stdin.readline().split())),
        ]
        grid_3x3[1].insert(1, None)
        answer = solve(grid_3x3)
        print(f'Case #{t}: {answer}')



def solve(g):
    prog = 0
    count = Counter()

    def _count(start, end):
        mid = (start+end)/2
        if mid == floor(mid):
            count[mid] += 1
    def _check(a, b, c):
        nonlocal prog
        if a+c == b<<1:
            prog += 1
    # Rows
    _check(g[0][0], g[0][1], g[0][2])
    _check(g[2][0], g[2][1], g[2][2])
    # Columns
    _check(g[0][0], g[1][0], g[2][0])
    _check(g[0][2], g[1][2], g[2][2])
    # Middle
    _count(g[0][0], g[2][2])
    _count(g[1][0], g[1][2])
    _count(g[0][1], g[2][1])
    _count(g[2][0], g[0][2])
    if count:
        num, cnt = count.most_common(1)[0]
        prog += cnt
    return prog


if __name__ == "__main__":
    main()