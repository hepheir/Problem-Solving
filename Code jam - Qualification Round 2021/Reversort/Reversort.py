import sys

def solve():
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    cost = 0
    for i in range(len(L)-1):
        j = L.index(min(L[i:]))
        L[i:j+1] = reversed(L[i:j+1])
        cost += j-i+1
    return cost


T = int(sys.stdin.readline())
for t in range(1, T+1):
    print(f'Case #{t}: {solve()}')