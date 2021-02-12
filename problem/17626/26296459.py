import sys

n = int(sys.stdin.readline().rstrip())

def solve(x, depth):
    if depth > 4: return
    for i in range(int(x**0.5), 0, -1):
        if i**2 < x//2:
            return
        left = x - i**2
        if int(left**0.5)**2 == left:
            print(depth)
            exit(0)
        solve(left, depth+1)

if int(n**0.5)**2 == n:
    print('1')
else:
    solve(n, 2)