def solve(n, k):
    stack = list(range(1,n+1))
    k -= 1
    pivot = 0
    while stack:
        pivot += k
        pivot %= len(stack)
        yield stack.pop(pivot)


N, K = map(int, input().split())

print('<'+', '.join(map(str,solve(N,K)))+'>')