import math
import sys

MOD = 1000000007


def mod_mult(a, b, mod):
    return (a % mod) * (b % mod) % mod


def solve():
    answer = 0

    M = int(sys.stdin.readline())
    for m in range(M):
        n, s = map(int, sys.stdin.readline().split())

        gcd = math.gcd(n, s)
        n //= gcd
        s //= gcd

        answer += mod_mult(s, pow(n, MOD-2, MOD), MOD)
    return answer % MOD


print(solve())
