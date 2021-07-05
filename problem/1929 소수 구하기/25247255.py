def is_prime(x:int) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)