import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

fibonacci_cache = [0, 1]
n_zeros_cache = [1, 0]
n_ones_cache = [0, 1]
def fibonacci(x):
    if len(fibonacci_cache) <= x:
        fib_x_2, n_zeros_2, n_ones_2 = fibonacci(x-2)
        fib_x_1, n_zeros_1, n_ones_1 = fibonacci(x-1)
        fibonacci_cache.append(fib_x_2+fib_x_1)
        n_zeros_cache.append(n_zeros_2+n_zeros_1)
        n_ones_cache.append(n_ones_2+n_ones_1)
    return fibonacci_cache[x], n_zeros_cache[x], n_ones_cache[x]

def solve():
    N = int(input())
    fib, n_zeros, n_ones = fibonacci(N)
    print(f'{n_zeros} {n_ones}')

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        solve()