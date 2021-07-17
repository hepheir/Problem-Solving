import math

prime_cache = [2,3,5,7,11,13,17,19]

def is_prime(x):
    if x in prime_cache:
        return True
    root = math.ceil(math.sqrt(x)+1)
    for i in range(2, root):
        if x % i == 0:
            return False
    prime_cache.append(x)
    prime_cache.sort()
    return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if is_prime(i):
        print(i)