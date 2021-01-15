import sys

def solve(h, w, n):
    n -= 1
    x = n // h + 1
    y = n % h + 1
    return f'{y}{x:02d}'

if __name__ == "__main__":
    for t in range(int(sys.stdin.readline())):
        H, W, N = map(int, sys.stdin.readline().split())
        print(solve(H, W, N))