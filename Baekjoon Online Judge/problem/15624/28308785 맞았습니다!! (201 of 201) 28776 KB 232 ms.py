MOD = int(1e9)+7


def solve():
    n = int(input())

    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(1, n):
        b, a = ((a+b) % MOD), (b % MOD)

    return b


print(solve())