def solve():
    MIN, MAX = map(int, input().split())
    # Make a part of Sieve of Eratosthenes
    offset = MIN
    size = MAX-MIN+1
    eratos = [True] * size
    for i in range(2, int(1e12**0.5)+1):
        square = i*i
        index = (square-offset) % square
        for j in range(index, size, square):
            eratos[j] = False
    # Count
    answer = 0
    for i in range(size):
        if eratos[i]:
            answer += 1
    return answer

print(solve())