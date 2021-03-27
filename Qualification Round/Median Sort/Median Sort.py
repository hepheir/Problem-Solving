import itertools
import sys


def ask(x1, x2, x3):
    print(x1, x2, x3)
    return int(sys.stdin.readline())


def median(*args):
    return sorted(args)[1]


def solve():
    mid = N // 2

T, N, Q = map(int, sys.stdin.readline().split())

L = list(range(1, N+1))

for t in range(1, T+1):
    solve()


x2 x1 x3
x3 x2 x4

x4 x3 x5