def make_eratos(size):
    eratos = [True] * (size + 1)
    eratos[0] = eratos[1] = False
    for i in range(2, int(size**0.5)+1):
        if eratos[i]:
            for j in range(2*i, size+1, i):
                eratos[j] = False
    return eratos


def solve():
    N = int(input())
    eratos = make_eratos(N)
    for prime in range(N+1):
        if not eratos[prime]:
            continue
        while N % prime == 0:
            print(prime)
            N //= prime
        if N == 1:
            break

solve()