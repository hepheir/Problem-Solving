import sys

for t in range(int(sys.stdin.readline())):
    H, W, N = map(int, sys.stdin.readline().split())
    N -= 1
    x = N // H + 1
    y = N % H + 1
    print(f'{y}{x:02d}')