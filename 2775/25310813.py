import sys

def solve(floor, room):
    upper = [0] * (room+1)
    lower = [i for i in range(room+1)]
    for f in range(floor):
        for r in range(1, room+1):
            upper[r] = upper[r-1] + lower[r]
        upper, lower = lower, upper
    return lower[room]


for t in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(solve(k, n))