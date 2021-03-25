def fibo(a, b, n):
    for n in range(n-1):
        a, b = b, a+b
    return a

def solve():
    D, K = map(int, input().split())
    for B in range(1, 100001):
        for A in range(1, B+1):
            if fibo(A, B, D) == K:
                print(A)
                print(B)
                return

solve()