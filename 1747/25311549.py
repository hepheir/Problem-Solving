def isPalindrome(x):
    x_str = str(x)
    for i in range(len(x_str)):
        if x_str[i] != x_str[-1-i]:
            return False
    return True

MAX_ANSWER = 1003001

n = int(input())

# Sieve of Eratosthenes
sieve = [True] * (MAX_ANSWER+2)
sieve[0] = False
sieve[1] = False
for i in range(2, int(MAX_ANSWER**0.5)+2):
    if sieve[i]:
        for j in range(2*i, MAX_ANSWER+2, i):
            sieve[j] = False

while True:
    if sieve[n] and isPalindrome(n):
        print(n)
        break
    n += 1