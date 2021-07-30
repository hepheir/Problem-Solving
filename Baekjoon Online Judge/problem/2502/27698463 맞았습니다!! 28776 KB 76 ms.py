def solve():
    D, K = map(int, input().split())
    for a in range(K-1, 0, -1):
        b = K
        for d in range(D-2):
            a, b = b-a, a
            if a > b:
                break
        else:
            print(a)
            print(b)
            return
solve()