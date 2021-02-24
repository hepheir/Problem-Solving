import sys
sys.setrecursionlimit(10**6)

memoization = {1: 0, 2: 1}

def solve(x):
    if x not in memoization:
        memoization[x] = 1 + min(solve(x//2)+x%2, solve(x//3)+x%3)
    return memoization[x]

N = int(sys.stdin.readline())

print(solve(N))
