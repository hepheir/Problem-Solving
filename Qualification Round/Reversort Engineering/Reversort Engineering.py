import sys

if DEBUG := True:
    import io
    sys.stdin = io.TextIOWrapper(io.BytesIO())
    sys.stdin.write('1\n7 27\n')
    sys.stdin.seek(0)

def solve():
    N, C = map(int, sys.stdin.readline().split())

    if C < (N-1):
        return 'IMPOSSIBLE'

    if C > (N-1)*(N-1)*N // 2:
        return 'IMPOSSIBLE'

    L = list(range(1, N+1))

    i, j = 0, N
    direction = True
    a, b = N-1, N-1
    while a < C:
        L[i:j] = reversed(L[i:j])
        if direction:
            j -= 1
        else:
            i += 1
        direction = not direction
        a, b = a+b, a-1


T = int(sys.stdin.readline())
for t in range(1, T+1):
    print(f'Case #{t}: {solve()}')