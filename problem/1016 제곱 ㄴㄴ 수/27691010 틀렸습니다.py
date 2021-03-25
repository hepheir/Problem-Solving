def solve():
    MIN, MAX = map(int, input().split())
    # Make a part of Sieve of Eratosthenes
    offset = MIN
    eratos = [True] * int(1e6+1)
    for i in range(2, int(1e12**0.5)+1):
        square = i*i
        index = square-offset
        if (index < 0):
            continue
        if (index >= len(eratos)):
            break
        if eratos[index]:
            for j in range(index, len(eratos), square):
                eratos[j] = False
    # Count
    answer = 0
    for i in range(MAX-MIN+1):
        if eratos[i]:
            answer += 1
    return answer

print(solve())