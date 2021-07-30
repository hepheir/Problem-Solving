def isPrime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True

input()
prime_numbers = [x for x in map(int, input().split()) if isPrime(x)]
print(len(prime_numbers))